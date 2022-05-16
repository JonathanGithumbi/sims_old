from pyexpat.errors import messages
from urllib.request import proxy_bypass
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from requests import delete
from . import forms
from user_account.models import CustomUser
from student.models import Student
from financial_account.models import FinancialAccount
from info.models import FeesStructure
from django.contrib.auth.models import BaseUserManager
import datetime 
from datetime import datetime,timedelta
from info.models import AcademicCalendar
import pytz
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import io
from django.http import FileResponse
from financial_account.models import CurrentBalance

@login_required
def admin_dashboard(request):
    """This view lands the user on  the administration dashboard"""
    """Displaying a list of functionalities afforded the administrator """
    return render(request,'administrator/admin_dashboard.html')

def date_range(start,end):
    """This view returns a list of datetime instances  of days between 'start' day and 'end' day """
    """It is used in get_term() to retrieve the term number """
    delta = end-start
    days = [start + timedelta(days=i) for i in range(delta.days+1)]
    return days


def get_term(date):
    """This method returns the term number (int) given the date """
    """Uses date_range() to retrieve the list of days in a term"""
    calendar = AcademicCalendar.objects.get(year=date.year)#This is the date provided from user.date_joined, during student registration
    term_1_start_date = calendar.term_1_start_date
    term_1_end_date = calendar.term_1_end_date
    term_2_start_date =calendar.term_2_start_date
    term_2_end_date = calendar.term_2_end_date
    term_3_start_date = calendar.term_3_start_date
    term_3_end_date = calendar.term_3_end_date

    term_1_days = date_range(term_1_start_date,term_1_end_date)
    term_2_days = date_range(term_2_start_date,term_2_end_date)
    term_3_days = date_range(term_3_start_date,term_3_end_date)

    if date in term_1_days:
        return 1
    if date in term_2_days:
        return 2
    if date in term_3_days:
        return 3


def get_term_amount(date,grade,lunch,transport):#Lunch and transport are optionals 
    """This function retrieves the fees due for a given term, provided the current date"""
    """it returns the amount due for a given term ther amount will be negative to indicate amout is due"""
    """This method is used only during student registration, a separate function get_term_amount_continous() calculates the amount for continuing students """
    #date is a datetime instance
    year = date.year#This is the date provided from user.date_joined, during student registration
    term = get_term(date)
    fee = FeesStructure.objects.get(year=2022,term=term,grade=grade)
    amount = fee.admission + fee.diary_and_report_book + fee.tuition_fee # the amount is the core_amount-'not optionals'
    if lunch and not transport:
        amount  = amount+ fee.hot_lunch
    if transport and not lunch:
        amount = amount + fee.transport
    if transport and lunch :
        amount = amount + fee.transport + fee.hot_lunch
    
    return -abs(amount)

def register_student(request):
    """This function registers a user, and associates that user to a student which is then associated with a financial account"""
    if request.method == 'GET':
        form = forms.StudentRegistrationForm()
        return render(request,'administrator/student_registration_page.html',{'form':form})
    if request.method =='POST':
        form = forms.StudentRegistrationForm(request.POST,request.FILES)# request.Files to retrieve the image file
        if form.is_valid():
            #Student registration logic
            # 1.create a user
            user = CustomUser()
            user.first_name = form.cleaned_data['first_name']
            user.middle_name = form.cleaned_data['middle_name']
            user.last_name = form.cleaned_data['last_name']
            password = CustomUser.objects.make_random_password()
            user.set_password(password)
            user.is_superuser = False
            user.username = form.cleaned_data['email']
            user.email = form.cleaned_data['email']
            user.is_staff = False
            user.is_active = True
            user.date_of_birth = form.cleaned_data['date_of_birth']
            user.gender = form.cleaned_data['gender']
            user.image = form.cleaned_data['image']
            user.is_administrator = False
            user.is_teacher = False
            user.is_student = True
            #save user
            user.save()

            # 2. Create the student
            student = Student()
            student.grade_admitted_to = form.cleaned_data['grade_admitted_to']
            student.current_grade = form.cleaned_data['grade_admitted_to']
            student.primary_contact_name = form.cleaned_data['primary_contact_name']
            student.primary_contact_phone_number = form.cleaned_data['primary_contact_phone_number']
            student.secondary_contact_name = form.cleaned_data['secondary_contact_name']
            student.secondary_contact_phone_number = form.cleaned_data['secondary_contact_phone_number']
            student.user = user
            #optionals
            student.hot_lunch = form.cleaned_data['hot_lunch']
            student.transport = form.cleaned_data['transport']
            student.save()

            # 3. Create the financial account
                    # - We need to know which term and year we are now given the date
                    # - calculate the core fees items without optioinals, if we have optionals, add them
                    # - create a financial account and Credit that amount to the student financial account
            transaction = FinancialAccount()
            transaction.student = student

            #optionals
            lunch = form.cleaned_data['hot_lunch']
            transport = form.cleaned_data['transport']

            year = user.date_joined.year
            month = user.date_joined.month
            day = user.date_joined.day
            date = datetime(year,month,day)

            #Making the datetime 'timezone aware', so that it can be used by get_term()
            date = date.replace(tzinfo=pytz.UTC)
            
            #Crediting the student the term's fees "+(-amount)"
            transaction.amount = get_term_amount(date,student.grade_admitted_to,lunch,transport)
            transaction.arrears = get_term_amount(date,student.grade_admitted_to,lunch,transport)
            transaction.transaction_type = 'credit'
            transaction.save()
            messages.add_message(request,messages.SUCCESS,"Student Registered Successfully")
            return HttpResponseRedirect(reverse('student_profile', args=[student.user.id]))
        else:
            return render(request,'administrator/student_registration_page.html',{'form':form})

@login_required
def student_profile(request,id):
    """this function displays the student's information including financial history"""
    """Gives access to  update, delete and downloading and printing of financial documents"""
    student = Student.objects.get(pk=id)
    return render(request, 'administrator/student_profile_page.html',{'student':student})

def search_student(request):
    """Searches for a given student given the first name and grade """
    if request.method == 'GET':
        form = forms.SearchStudentForm()
        return render(request, 'administrator/search_student_page.html',{'form':form})
    if request.method == 'POST':
        form = forms.SearchStudentForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            
            grade = form.cleaned_data['grade']

            if grade and not first_name :
                students = Student.objects.filter(current_grade=grade)
                return render(request, 'administrator/search_results_page.html',{'students':students})
            if grade and first_name:
                students = Student.objects.filter(current_grade=grade).filter(user__first_name__iexact = first_name)
                return render(request, 'administrator/search_results_page.html',{'students':students})
            
        else:
            return render(request, 'administrator/search_student_page.html',{'form':form})
            
def update_student(request,id):
    """Updates student details """
    student = Student.objects.get(pk=id)
    user = CustomUser.objects.get(pk=student.user.id)
    if request.method == 'GET':
        data = {
            'first_name' : user.first_name,
            'middle_name' : user.middle_name,
            'last_name' : user.last_name, 
            'gender' : user.gender,
            'image' : user.image,
            'email' : user.email,
            'date_of_birth' : user.date_of_birth,
            'grade_admitted_to' :  student.grade_admitted_to,
            'primary_contact_name' : student.primary_contact_name,
            'primary_contact_phone_number' : student.primary_contact_phone_number,
            'secondary_contact_name' : student.secondary_contact_name,
            'secondary_contact_phone_number' : student.secondary_contact_phone_number,
            'hot_lunch' : student.hot_lunch,
            'transport' : student.transport
        }
        form = forms.StudentRegistrationForm(data)
        return render(request, 'administrator/student_update_page.html',{'form':form,'student':student})
    if request.method == 'POST':
        form = forms.StudentRegistrationForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.middle_name = form.cleaned_data['middle_name']
            user.last_name = form.cleaned_data['last_name']
            user.gender = form.cleaned_data['gender']
            user.image = form.cleaned_data['image']
            user.email = form.cleaned_data['email']
            user.date_of_birth = form.cleaned_data['date_of_birth']
            student.grade_admitted_to = form.cleaned_data['grade_admitted_to']
            student.primary_contact_name = form.cleaned_data['primary_contact_name']
            student.primary_contact_phone_number = form.cleaned_data['primary_contact_phone_number']
            student.secondary_contact_name = form.cleaned_data['secondary_contact_name']
            student.secondary_contact_phone_number = form.cleaned_data['secondary_contact_phone_number']
            student.hot_lunch = form.cleaned_data['hot_lunch']
            student.transport = form.cleaned_data['transport']
            user.save()
            student.save()

            messages.add_message(request,messages.SUCCESS,"Student Information Updated Successfully")
            
            return redirect(reverse('student_profile', args=[student.user.id]))
        else:
            return render(request, 'administrator/student_update_page.html',{'form':form})

def delete_student(request, id):
    """Deletes a user which deletes the student which deletes the account"""
    user = CustomUser.objects.get(pk=id)
    user.delete()
    messages.add_message(request,messages.SUCCESS,'Student Deleted Successfully')
    return redirect(reverse('administrator_dashboard'))


def make_payment(request,id):
    """Making debit transactions"""
    """This is used for debiting amounts to a student's account"""
    student = Student.objects.get(pk=id)
    if request.method == 'GET':
        form = forms.MakePaymentForm()
        return render(request, 'administrator/make_payment_page.html',{'form':form,'student':student})
    if request.method == 'POST':
        form = forms.MakePaymentForm(request.POST)
        if form.is_valid():
            prev_transaction = student.financialaccount_set.order_by('-date_of_payment').first()
            print(prev_transaction.amount)
            prev_arrears = prev_transaction.arrears
            arrears = prev_arrears + form.cleaned_data['amount']
            transaction = student.financialaccount_set.create(
            transaction_type = 'debit',
            amount = form.cleaned_data['amount'],
            arrears = arrears,
            student = student ,
            )
            transaction.save()
            messages.add_message(request,messages.SUCCESS,'Payment made successfully')
            return redirect(reverse('student_profile',args=[student.user.id]))
        else:
            return render(request,'administrator/make_payment_page.html',{'form':form,'student':student})


def transaction_details(request, id ):
    """displays transaction details and allows you to print/download receipt for a payment """
    transaction = FinancialAccount.objects.get(pk=id)
    return render(request,'administrator/transaction_details.html',{'transaction':transaction})
        

def download_statement(request, id):
    """downloads/prints a financial history statement for a given student"""
    """Generate Statement"""
    pass

def download_receipt(request, id):
    """downloads/prints a receipt for a given transaction"""
    """Generate PDF"""
    pass
    
def reports(request):
    """displays options to display and print reports {'students with high arrears','students taking hot lunch this term','students taking transport this year'}"""
    return render(request, 'administrator/reports.html')

def lunch_report(request):
    students = Student.objects.filter(hot_lunch=True)
    return render(request, 'administrator/lunch_report.html',{'students':students})

def transport_report(request):
    students = Student.objects.filter(transport=True)
    return render(request, 'administrator/transport_report.html',{'students':students})

def fees_arrears_report(request):
    # get a list of all the students whose arrears is greater than 0
    # make sure to get the latest transaction for a given student
    records = CurrentBalance.objects.filter(current_balance__lt = 0).order_by('-current_balance')
    return render(request, 'administrator/fees_Arrears_report.html',{'records':records})


def fees_structure(request):
    """Displays the current fees structure fo a give year,term"""
    return render(request, 'administrator/fees_structure.html')

def academic_calendar(request):
    return render(request, 'administrator/academic_calendar.html')

def notifications(request):
    return render(request, 'administrator/notifications.html')




