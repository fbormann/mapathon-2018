from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

def checkIfInsidePolygon(polygon_lat_list, polygon_lng_list, user_lat, user_lng):
    lons_lats_vect = np.column_stack((polygon_lat_list, polygon_lng_list)) # Reshape coordinates
    polygon = Polygon(lons_lats_vect) # create polygon
    point = Point(float(user_lat), float(user_lng)) # create point
    return polygon.contains(point)
    