"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 27/11/2021
"""

# Import neded packages
from flask import Blueprint, session, request
from flask.helpers import flash
from flask.templating import render_template


# Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import checkValue


# Definition of the blueprint
programBP = Blueprint('programBP', __name__)


# Definition the program route
@programBP.route('/defineProgram', methods=['GET', 'POST'])
def define_program():
    if request.method == 'GET':
        userData = programBPUserData(session['id'])

        if checkValue('users', 'id', session['id']):
            return render_template('referenceProgram.html', userData=userData)
        else:
            flash("Une erreur est survenue. Merci de réessayer.", "Red_flash")
            return render_template('home.html')
    
    elif request.method == 'POST':
        programContent = request.form['programmArea']

        if not checkValue('programs', 'user_id', session['id']):
            addQuery = '''INSERT INTO programs (user_id, content) VALUES (?, ?);'''
            args = (session['id'], programContent)

        else:
            addQuery = '''UPDATE programs SET content=? WHERE user_id=?;'''
            args = (programContent, session['id'])
        
        db, cursor = connectDatabase()

        cursor.execute(addQuery, args)
        db.commit()
        cursor.close()
        db.close()

        userData = programBPUserData(session['id'])

        return render_template('referenceProgram.html', userData=userData)
    
    else:
        return render_template('home.html')



# Definition of usefull functions for this BluePrint only


def programBPUserData(session_id: str) -> dict:
    """
        Functions to return the userData used in the program route in the program BP.

        Arguments:
            - session_id (string) : user's session id
        
        Returns :
            - userData (dict) : needed dict for the program page
    """
    db, cursor = connectDatabase()
    programContent = ""

    query = '''SELECT firstName, lastName FROM users WHERE id=?;'''
    arg = (session_id, )

    cursor.execute(query, arg)
    for userTuple in cursor.fetchall():
        userFirstName = userTuple[0]
        userLastName = userTuple[1]
        
    query = '''SELECT content FROM programs WHERE user_id=?;'''
    arg = (session_id, )

    cursor.execute(query, arg)
    for userTuple in cursor.fetchall():
        programContent = userTuple[0]
        
    db.close()

    userData = {
        'name': userFirstName+" "+userLastName,
        'program': programContent
    }

    return userData