from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render (request,'Home/index.html')

def about(request):
    return render(request,'Home/about.html')

def check(request):
    return render(request,'Home/check.html')

def service(request):
    return render(request,'Home/service.html')

def program(request):
    return render(request,'Home/program.html')

def contact(request):
    return render(request,'Home/contact.html')

# def register(request):
#     return render(request,'Register/register.html')