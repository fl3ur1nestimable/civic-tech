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


# Import personnal modules
from python.database.connectDatabase import connectDatabase



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

    returnJson = {
        'lat': my_json['latitude'],
        'lon': my_json['longitude']
    }

    return returnJson


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

    coordinate_url = f"{lon1}%2C{lat1}%3B{lon2}%2C{lat2}?"
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


def shortest_time(data: dict, v: dict) -> dict:
    """
        Function to calculate the closest point in travel time from a dictionnary to a given point

        Arguments :
            - data (dict) : a dictionnary of coordinate
            - v (dict) : the coordinate to find the closest point
        
        Returns :
            - closestPoint (dict) -> the closest point found
    """
    
    shortestTime = 0
    closestPoint = {
        "name": "",
        "lat": 0,
        "lon": 0
    }

    for items in data:
        tempTime = best_duration(data[items]['lat'], data[items]['lon'], v['lat'], v['lon'])
        
        if shortestTime == 0:
            shortestTime = tempTime
            closestPoint['name'] = items
            closestPoint['lat'] = data[items]['lat']
            closestPoint['lon'] = data[items]['lon']
        
        elif tempTime < shortestTime:
            shortestTime = tempTime
            closestPoint['name'] = items
            closestPoint['lat'] = data[items]['lat']
            closestPoint['lon'] = data[items]['lon']
    
    return closestPoint


def find_closest_vote_office(coordinate: dict) -> dict:
    dataDict = {}

    query = '''SELECT * FROM Vote_office'''

    db, cursor = connectDatabase()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()

    for voteOffice in data:
        dataDict[voteOffice[3]] = {}
        dataDict[voteOffice[3]]['lat'] = voteOffice[1]
        dataDict[voteOffice[3]]['lon'] = voteOffice[2]

    closestVoteOffice = shortest_time(dataDict, coordinate)

    return closestVoteOffice