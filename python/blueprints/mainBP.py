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

# Definition of the blueprint
mainBP = Blueprint('mainBP', __name__)


# Definition of the main route
@mainBP.route('/')
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
    
    jobAbrev={
        "agriexp": 'Agriculteur exploitant',
        "artcomchef": "Artisan, Commerçant, Chef d'entreprise",
        "cadreprofintsup": 'Cadre, Profession intellectuelle supérieure',
        "profintermed": 'Profession intermédiaire',
        "employe": 'Employé',
        "ouvrier": 'Ouvrier',
        "retraite": 'Retraité',
        "sansactprof": 'Sans activité professionnelle'
    }

    return render_template('home.html', edges=edges, jobAbrev=jobAbrev)