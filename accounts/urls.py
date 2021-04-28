from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from accounts.forms import *
app_name = 'accounts'

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm),name='login'),
    path('signIn/',signIn,name='signIn'),
]
