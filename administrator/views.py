from django.shortcuts import render
from . import forms
from user_account.models import CustomUser
from student.models import Student
from financial_account.models import FinancialAccount
from django.contrib.auth.models import BaseUserManager
import datetime 

def admin_dashboard(request):
    return render(request,'administrator/admin_dashboard.html')

def get_term_amount(date):
    """This function retrieves the fees due for a given term, provided the current date"""
    pass



def register_student(request):
    """a student must have a financial account and must be able to opt a student out of optional fees items"""
    if request.method == 'GET':
        form = forms.StudentRegistrationForm()
        return render(request,'administrator/student_registration_page.html',{'form':form})
    if request.method =='POST':
        form = forms.StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            #Student registration logic
            # 1.create a user
            user = CustomUser()
            user.first_name = form.cleaned_data['first_name']
            user.middle_name = form.cleaned_data['middle_name']
            user.last_name = form.cleaned_data['last_name']
            password = BaseUserManager.make_random_password()
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
            user = user.save()

            # 2. Create the student
            student = Student()
            student.grade_admitted_to = form.cleaned_data['grade_admitted_to']
            student.current_grade = form.cleaned_data['grade_admitted_to']
            student.primary_contact_name = form.cleaned_data['primary_contact_name']
            student.primary_contact_phone_number = form.cleaned_data['primary_contact_phone_number']
            student.secondary_contact_name = form.cleaned_data['secondary_contact_name']
            student.seconday_contact_phone_number = form.cleaned_data['seconday_contact_phone_number']
            student.user = user
            student.save()

            # 3. Create the financial account
                    # - We need to know which term and year we are now given the date
                    # - calculate the core fees items without optioinals, if we have optionals, add them
                    # - create a financial account and Credit that amount to the student financial account
            account = FinancialAccount()
            account.student = student
            account.amount = get_term_amount(datetime.date.today())
                    
        if not form.is_valid:
            return render(request,'administrator/student_registration_page.html',{'form':form})