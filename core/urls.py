from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/request/lat=<lat>,lng=<lng>', views.competitionRequest, name='competition_request')
]
