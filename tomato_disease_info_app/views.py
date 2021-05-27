from django.shortcuts import render
from django.shortcuts import redirect,render
# Create your views here.

def disease_info(request):
    return render(request, 'disease_info.html')

def info_page(request):
    return render(request, 'info.html')