from django.shortcuts import render

# Create your views here.
def mainPage(request):
    print(request.user.is_authenticated)
    return render(request,'main.html')



