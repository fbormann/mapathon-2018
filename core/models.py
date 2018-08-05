from django.db import models

class Polygon(models.Model):
    mapathon = models.ForeignKey('Mapathon', related_name='polygon', on_delete=models.CASCADE)

class Point(models.Model):
    order = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    polygon = models.ForeignKey('Polygon', related_name='points', on_delete=models.CASCADE)


class Mapathon(models.Model):
    name = models.CharField(max_length=120)
    goal = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)