from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Polygon, Point, Mapathon, ResultSubmission
from .utils import checkIfInsidePolygon
from django.core import serializers

def index(request):
    context = {}
    return render(request, 'core/index_admin.html', context)

def competitionRequest(request, lat, lng):
    user_lat = lat
    user_lng = lng
    polygons = Polygon.objects.all()
    points_lat = []
    points_lng = []
    mapathon = None
    mapathon_response = {}
    for polygon in polygons:
        for point in polygon.points.all().order_by('order'):
            points_lat.append(point.lat)
            points_lng.append(point.lng)
        
        if checkIfInsidePolygon(points_lat, points_lng, user_lat, user_lng) or True:
            mapathon = serializers.serialize("json", Mapathon.objects.filter(id=polygon.mapathon.id))
            mapathon_data = Mapathon.objects.get(id=polygon.mapathon.id)
            mapathon_response["name"] = mapathon_data.name
            mapathon_response["goal"] = mapathon_data.goal
            mapathon_response = json.dumps(mapathon_response)
            break
        else:
            mapathon_response = '{"status": 401}'

    return HttpResponse(mapathon_response, content_type="application/json")

@csrf_exempt
def createCompetition(request):
    polygon_points = json.loads(request.POST['polygon_points'])
    competition_name = request.POST['competition_name']
    competition_goal = request.POST['competition_goal']
    mapathon = Mapathon(name = competition_name, goal= competition_goal)
    mapathon.save() #created competition

    polygon = Polygon(mapathon= mapathon)
    polygon.save()

    order = 0
    for point in polygon_points:
        new_point = Point(order=order, lat=point["lat"], lng = point["lng"], polygon=polygon)
        order += 1 
        new_point.save()
    
    return redirect("list_submissions", id=mapathon.id)

@csrf_exempt
def receiveResponse(request):
    data = request.POST
    mapathon = Mapathon.objects.get(name=data["name"])
    submission = ResultSubmission(description=data["description"], category=data["category"], 
    lat=float(data["latitude"]), lng=float(data["longitude"]), title= data["title"], mapathon=mapathon)
    submission.save()
    return JsonResponse(data, status=200)

def listSubmissions(request, id):
    mapathon = Mapathon.objects.get(id=id)
    submissions = mapathon.submissions.all()
    context = {}
    context["submissions"] = submissions
    return render(request, "core/competition_list.html", context)