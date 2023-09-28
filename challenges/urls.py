from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_challenge),
    path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenge, name = 'challenges_url_name'),
]
