from django.shortcuts import render
from .forms import *

# Create your views here.
def signIn(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'signIn.html',{'new_user':new_user})
    else:
        user_form = RegisterForm()
    
    return render(request,'signIn.html',{'form':user_form})


