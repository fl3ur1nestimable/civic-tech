"""
    Author : Antoine Yebouet
    Mail : antoine.yebouet@telecomnancy.eu
    Date : 06/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from werkzeug.utils import redirect


#Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import checkValue

#Definition of the blueprint
progFull= Blueprint('progFull',__name__)


@progFull.route('/program0')
def program0():
    nomCandidat=request.args.get('nomCandidat')
    prenomCandidat=request.args.get('prenomCandidat')
    data=[nomCandidat,prenomCandidat]
    db, cursor =connectDatabase()
    query = '''SELECT  FROM users WHERE ;'''

    session['data']=data
    return redirect(url_for('progFull.program'))


@progFull.route('/program')
def program():
    data=session.get('data',None)
    nomCandidat=data[0]
    prenomCandidat=data[1]
    prog=data[2]
    return render_template('program.html',nomCandidat=nomCandidat,prenomCandidat=prenomCandidat,prog=prog)