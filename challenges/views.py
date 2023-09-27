from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def january(request):
    return HttpResponse("eat no meats for the entire of the month!")

def february(request):
    return HttpResponse("walk for at least 30 minutes every day!")