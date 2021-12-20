"""
    Author : Antoine Yebouet
    Mail : antoine.yebouet@telecomnancy.eu
    Date : 06/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request
from flask.helpers import flash
from flask.templating import render_template


#Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import checkValue
from py.core.truncatePrograms import truncatePrograms

#Definition of the blueprint
progFullBP = Blueprint('progFullBP',__name__)


@progFullBP.route('/program/<string:firstName>/<string:lastName>/<int:id>')
def program(firstName: str, lastName: str, id: int) -> str:
    query = '''SELECT l.program FROM Candidate AS c JOIN List AS l ON c.listId=l.id WHERE c.id=?;'''
    arg = (id, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)

    prog = cursor.fetchall()[0][0]

    db.close()


    return render_template('program.html',nomCandidat=firstName,prenomCandidat=lastName,prog=prog)