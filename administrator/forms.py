from django import forms
from grade.models import Grade

class StudentRegistrationForm(forms.Form):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female')
    )
    first_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    image = forms.ImageField(required=False)
    email =forms.EmailField()
    date_of_birth = forms.DateField()
    grade_admitted_to = forms.ModelChoiceField(queryset=Grade.objects.all())
    primary_contact_name = forms.CharField( max_length=30)
    primary_contact_phone_number = forms.CharField( max_length=30)
    secondary_contact_name = forms.CharField( max_length=30, required=False)
    secondary_contact_phone_number = forms.CharField( max_length=30, required=False)
    hot_lunch = forms.BooleanField(required=False)
    transport = forms.BooleanField(required=False)

class SearchStudentForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    grade =  forms.ModelChoiceField(queryset=Grade.objects.all())

class TeacherRegistrationForm(forms.Form):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female')
    )
    first_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    image = forms.ImageField(required=False)
    email =forms.EmailField()
    date_of_birth = forms.DateField()
    

class MakePaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=8,decimal_places=2)
    # Transaction number for  API call to paybill/bank acc, for confirmation of transaction status
    #transaction_number = forms.IntegerField()
    