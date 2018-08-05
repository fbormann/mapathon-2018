from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('competitions/request', name='competition_request')
]
