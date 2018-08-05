from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    context = {}
    return render(request, 'core/index_admin.html', context)

def competitionRequest(request, lat, lng):
    user_lat = lat
    user_lng = lng
    return JsonResponse({'lat': lat, 'lng': lng})

