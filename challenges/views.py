from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def monthly_challenges(request, month):
    monthly_challenge = None
    if month == "february":
        monthly_challenge = "walk for at least 30 minutes every day!"
    elif month == "january":
        monthly_challenge = "eat no meats for the entire of the month!"
    elif month == "march":
        monthly_challenge = "it's you're birthday month! just have fun :)"
    else:
        monthly_challenge = "this month is not defined"
    return HttpResponse(monthly_challenge)