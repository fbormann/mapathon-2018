from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Polygon, Point, Mapathon
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
    for polygon in polygons:
        print(polygon)
        for point in polygon.points.all().order_by('order'):
            points_lat.append(point.lat)
            points_lng.append(point.lng)
        
        if checkIfInsidePolygon(points_lat, points_lng, user_lat, user_lng):
            mapathon = serializers.serialize("json", Mapathon.objects.filter(id=polygon.mapathon.id))
            break
        else:
            mapathon= {"status": 401}

    return HttpResponse(mapathon, content_type="application/json")

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
    
    return JsonResponse(data={"success": "ok"},status=200)