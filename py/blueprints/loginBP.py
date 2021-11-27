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
login = Blueprint('login', __name__)


# Definition of the login route
@login.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']
        remember = request.form['remember']
        userFound = False

        query = '''SELECT id, role, password FROM users WHERE identifier=?;'''
        arg = (identifier, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)
        for userTuple in cursor.fetchall():
            userFound = True
            userId = userTuple[0]
            userRole = userTuple[1]
            userPassword = userTuple[2]
        db.close()

        if userFound and check_password_hash(userPassword, password):
            if remember:
                session['id'] = userId
                session['role'] = userRole

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
@login.route('/logout')
def logout():
    session['id'] = None
    session['role'] = None
    return render_template('home.html')
