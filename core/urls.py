from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/request/lat=<lat>,lng=<lng>', views.competitionRequest, name='competition_request'),
    path('competitions/create', views.createCompetition, name='create_competition'),
    path('competitions/submit', views.receiveResponse, name="receive_response"),
    path("competitions/results/<int:id>", views.listSubmissions, name="list_submissions")
]
