"""
    Author : Cheneviere Thibault, Guillot Thom
    Mail : thibault.cheneviere@telecomnancy.eu, thom.guillot@telecomnancy.eu
    Date : 17/12/2021
"""

# Import neded packages
from flask import Blueprint
from flask.templating import render_template

#Import personal modules
from python.database.connectDatabase import connectDatabase
from python.core.sortbyPoliticalEdge import sortbyPoliticalEdge
from python.core.coreLocalisation import get_map_src

# Definition of the blueprint
mainBP = Blueprint('mainBP', __name__)


# Definition of the main route
@mainBP.route('/')
@mainBP.route('/home')
def home() -> str:
    db, cursor = connectDatabase()

    query = '''
    SELECT * FROM Candidate AS c 
    JOIN List AS l ON l.id = c.listId 
    JOIN ProgramGrade AS pg ON pg.listID = l.id
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    db.close()

    edges = sortbyPoliticalEdge(data)
    return render_template('home.html', edges=edges)

@mainBP.route('/card')
def card():
    data = {
        "start": {
            "lat": 6.168813538550233,
            "lon": 48.685992319231566,
            "name": "Boulangerie de la commanderie"
        },
        "end": {
            "lat": 6.171844361204282,
            "lon": 48.68661195429168,
            "name": "Le chat noir"
        }
    }
    
    return render_template('map.html', data=data)