"""
    Author : Cheneviere Thibault, Guillot Thom
    Mail : thibault.cheneviere@telecomnancy.eu, thom.guillot@telecomnancy.eu
    Date : 30/12/2021
"""

# Import neded packages
from flask import Blueprint, request
from flask.templating import render_template

#Import personal modules
from python.database.connectDatabase import connectDatabase
from python.core.coreLocalisation import find_closest_vote_office, get_location

# Definition of the blueprint
mapBP = Blueprint('mapBP', __name__)


# Definition of the map route
@mapBP.route('/map/<string:travelType>')
def card(travelType= str) -> str:
    if request.method == 'GET':
        userIp = request.remote_addr

        userCoordinate = get_location(userIp)

        closestVoteOffice = find_closest_vote_office(userCoordinate)

        data = {
            "start": {
                "lon": userCoordinate['lon'],
                "lat": userCoordinate['lat'],
                "name": "Votre position"
            },
            "end": {
                "lat": closestVoteOffice['lat'],
                "lon": closestVoteOffice['lon'],
                "name": "Le chat noir"
            }
        }

        emojiData = {
            "walking": "🚶",
            "cycling": "🚲",
            "driving": "🚗"
        }
        
        return render_template('map.html', data=data, travelType=travelType, emoji=emojiData[travelType])