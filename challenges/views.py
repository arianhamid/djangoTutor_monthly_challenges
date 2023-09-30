from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}
# Create your views here.


def index_challenge(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Please enter a valid month number")
    redirect_month = months[month-1]
    redirect_path = reverse("challenges_url_name", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {'challenge_text': challenge_text, 'title': month})
    except:
        # error_message = render_to_string('404.html')
        # return HttpResponseNotFound(error_message)
        raise Http404()
