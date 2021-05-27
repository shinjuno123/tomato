from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
app_name = 'tomato_disease_info_app'

urlpatterns = [
    path('tomato_disease_info/', disease_info, name='tomato_disease_info'),
    path('tomato_disease_info/info_page', info_page, name='info' )
    
]
