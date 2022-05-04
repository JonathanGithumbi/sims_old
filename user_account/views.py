from audioop import reverse
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from user_account.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index_page'))
        else:
            context = {'message':'user is none'}
            return render(request,'user_account/login.html',context)
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'user_account/login.html',{'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_page'))