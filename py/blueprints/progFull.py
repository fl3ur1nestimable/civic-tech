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
progFull= Blueprint('progFull',__name__)


@progFull.route('/program')
def program():
    nomCandidat=request.args.get('nomCandidat')
    prenomCandidat=request.args.get('prenomCandidat')
    prog=request.args.get('prog')
    return render_template('program.html',nomCandidat=nomCandidat,prenomCandidat=prenomCandidat,prog=prog)