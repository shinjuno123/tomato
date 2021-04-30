from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import *
# Create your views here.
def signUp(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
        return redirect('mainApp:mainApp')

    else:
        signup_form = UserCreationForm()
    
    return render(request,'signUp.html',{'signup_form':signup_form})



def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            print("로그인됨")
        return redirect('mainApp:mainApp')

    else:
        login_form = AuthenticationForm()

    return render(request,'login.html',{'login_form':login_form})



def logout(request):
    auth_logout(request)
    return redirect('mainApp:mainApp')