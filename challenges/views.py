from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "walk for at least 30 minutes every day!",
    "february": "cock for at least 30 minutes every day!",
    "march": "it's you're birthday month! just have fun :)",
    "april": "cock for at least 30 minutes every day!",
    "may": "walk for at least 30 minutes every day!",
    "jun": "cock for at least 30 minutes every day!",
    "july": "eat no meats for the entire of the month!",
    "august": "cock for at least 30 minutes every day!",
    "september": "walk for at least 30 minutes every day!",
    "november": "eat no meats for the entire of the month!",
    "october": "cock for at least 30 minutes every day!",
    "december": "cock for at least 30 minutes every day!",
}
# Create your views here.


def monthly_challenges_by_number(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("Please enter a valid month number")
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")
