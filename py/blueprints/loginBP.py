"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint, request, session
from flask.helpers import flash
from flask.templating import render_template
from werkzeug.security import check_password_hash



# Import personnal modules
from py.database.connectDatabase import connectDatabase


# Definition of the blueprint
loginBP = Blueprint('loginBP', __name__)


# Definition of the login route
@loginBP.route('/login', methods=['GET', 'POST'])
def login() -> str:
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']

        userFound = False

        query = '''SELECT id, password FROM users WHERE identifier=?;'''
        arg = (identifier, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)
        for userTuple in cursor.fetchall():
            userFound = True
            userId = userTuple[0]
            userPassword = userTuple[1]
        db.close()

        if userFound and check_password_hash(userPassword, password):
            session['id'] = userId

            flash("You have succesfully logged in.", "Green_flash")
            return render_template('home.html')
            
        elif not userFound:
            flash("You have a wrong identifier, please try again.", "Red_flash")
            return render_template('login.html')

        else:
            flash("You have a wrong password, please retry.", "Red_flash")
            return render_template('login.html')

    return render_template('login.html')


# Definition of the logout route
@loginBP.route('/logout')
def logout() -> str:
    session['id'] = None
    session['role'] = None
    return render_template('home.html')
