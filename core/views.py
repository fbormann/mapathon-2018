from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'core/index_admin.html', context)

def competitionRequest(request):
    user_lat = request["lat"]
    user_lng = request["lng"]
    return None

