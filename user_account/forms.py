from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

#this is a model form that inherits from user creation form
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'middle_name',
            'last_name',
        ]
        exclude = ['password1','password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
    