"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/12/2021
"""

# Import needed packages
import requests
import json
from math import cos, asin, sqrt, pi
from urllib.parse import urlencode



def get_location(ipAdress: str) -> dict:
    """
        Function to return latitude and longitude of a given ip adress

        Arguments :
            - ipAdress (string) : a given ip adress

        Returns :
            - data (dict) : the longitude and latitude of the given ip adress
    """
    request = "https://ipgeolocation.abstractapi.com/v1/?api_key=94a3f5a8eece44a58fa30d617d3eb123&fields=latitude,longitude&ip_adress=" + ipAdress

    response = requests.get(request)

    data = response.content.decode('utf8')
    my_json = json.loads(data)

    return my_json


def distance(lat1: int, lon1: int, lat2: int, lon2: int) -> int:
    """
        Functions to calculate the distance between two points of the globe using the Haversine formula

        Arguments:
            - lat1 (integer) : first latitude coordinate
            - lon1 (integer) : first longitude coordinate
            - lat2 (integer) : second latitude coordinate
            - lon2 (integer) : second longitude coordinate
        
        Returns :
            - d (integer) : distance between two given points
    """
    p = pi/180
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))


def closest(data: dict, v: dict) -> dict:
    """
        Function to calculate the closest point in distance from a dictionnary to a given point

        Arguments :
            - data (dict) : a dictionnary of coordinate
            - v (dict) : the coordinate to find the closest point
        
        Returns :
            - closestPoint (dict) -> the closest point found
    """
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))


def best_duration(lat1: int, lon1: int, lat2: int, lon2: int) -> int:
    """
        Function to calculate the best travel time between two points

        Arguments:
            - lat1 (integer) : first latitude coordinate
            - lon1 (integer) : first longitude coordinate
            - lat2 (integer) : second latitude coordinate
            - lon2 (integer) : second longitude coordinate
        
        Returns :
            - best_duration (integer) : best travel time between two points in seconds
    """

    apiKey = "pk.eyJ1IjoidGhpYmF1bHQtMjMiLCJhIjoiY2t4bG0xNHV1MWRobTJxcGVseWx1dGhoNSJ9.s7HzfDQrQPWrY8d5A4oivA"
    main_url = "https://api.mapbox.com/directions/v5/mapbox/walking/"

    params = {
        "access_token": apiKey,
        "alternatives": "true",
        "geometries": "geojson",
        "language": "fr",
        "overview": "simplified",
    }

    coordinate_url = f"{lat1}%2C{lon1}%3B{lat2}%2C{lon2}?"
    params_url = urlencode(params)

    complete_url = main_url + coordinate_url + params_url

    response = requests.get(complete_url)

    data = response.content.decode('utf8')
    my_json = json.loads(data)

    best_duration = my_json['routes'][0]['duration']

    for routes in my_json['routes']:
        if routes['duration'] < best_duration:
            best_duration = routes['duration']
    
    return best_duration


def closest_time(data: dict, v: dict) -> dict:
    """
        Function to calculate the closest point in travel time from a dictionnary to a given point

        Arguments :
            - data (dict) : a dictionnary of coordinate
            - v (dict) : the coordinate to find the closest point
        
        Returns :
            - closestPoint (dict) -> the closest point found
    """
    return min(data, key=lambda p: best_duration(v['lat'],v['lon'],p['lat'],p['lon']))


def get_map_src(lat: int, lon: int) -> str:

    apiKey = "pk.eyJ1IjoidGhpYmF1bHQtMjMiLCJhIjoiY2t4bG0xNHV1MWRobTJxcGVseWx1dGhoNSJ9.s7HzfDQrQPWrY8d5A4oivA"
    main_url = "https://api.mapbox.com/styles/v1/mapbox/streets-v10/static/"

    params = {
        "access_token": apiKey
    }

    params_url = urlencode(params)
    coordinate_url = f"{lat},{lon},15/500x300@2x?"

    complete_url = main_url + coordinate_url + params_url

    response = requests.get(complete_url)
    print(response)

    return complete_url