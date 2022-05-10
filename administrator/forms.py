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

    