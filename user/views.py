from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


def payment(request):
    return render(request,'user/payment.html')

def high(request):
    return render(request,'user/high.html')

def medium(request):
    return render(request,'user/medium.html')

def low(request):
    return render(request,'user/low.html')