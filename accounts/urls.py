from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from accounts.forms import *
app_name = 'accounts'

urlpatterns = [
    path('login/',login,name='login'),
    path('signUp/',signUp,name='signUp'),
    path('logout/',logout,name='logout')
]
