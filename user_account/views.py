from django.shortcuts import render

from django.contrib.auth import views as auth_views

from user_account.forms import LoginForm

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
