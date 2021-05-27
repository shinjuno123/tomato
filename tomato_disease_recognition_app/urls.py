from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
app_name = 'tomato_disease_recognition_app'

urlpatterns = [
    path('tomato_disease_recognition/',login,name='tomato_disease_recognition'),

]
