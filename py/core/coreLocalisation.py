"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/12/2021
"""

# Import needed packages
import requests
import json
from math import cos, asin, sqrt, pi



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

    my_json = response.content.decode('utf8')
    data = json.loads(my_json)

    return data


def distance(lat1: int, lon1: int, lat2: int, lon2: int) -> int:
    """
        Functions to calculate the distance between two points of the globe using the Haversine formula

        Arguments:
            - lat1 (integer) : first latitude coordinate
            - lon1 (integer) : first longitude coordinate
            - lat2 (integer) : second latitude coordinate
            - lon2 (integer) : second longitude coordinate
    """
    p = pi/180
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))


def closest(data: dict, v: dict) -> dict:
    """
        Function to calculate the closest point in a dictionnary from a given point

        Arguments :
            - data (dict) : a dictionnary of coordinate
            - v (dict) : the coordinate to find the closest point
        
        Returns :
            - closestPoint (dict) -> the closest point found
    """
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))
