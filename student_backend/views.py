from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request)
 

def profile(request):
    return render(request)


def groups(request):
    return render(request)


def subject(request):
    return render(request)

def calendar(request):
    return render(request)

def grades(request):
    return render(request)


def settings(request):
    return render(request)
