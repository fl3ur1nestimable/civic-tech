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
    data = {'lat': 6.185197596754502, 'lon': 48.69196558832937, 'name': 'Le Chat Noir'}
    data_src = {
        "src": get_map_src(data['lat'], data['lon']),
        "name": data['name']
    }
    return render_template('card.html', data=data_src)