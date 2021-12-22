"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint, request, session, redirect
from flask.helpers import flash
from flask.templating import render_template
from werkzeug.security import check_password_hash
import os


# Import personnal modules
from py.database.connectDatabase import connectDatabase
from py.core.fileStorage import save_candidate_picture


# Definition of the blueprint
loginBP = Blueprint('loginBP', __name__)


# Definition of the login route
@loginBP.route('/login', methods=['GET', 'POST'])
def login() -> str:
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']

        userFound = False

        query = '''SELECT id, password FROM Candidate WHERE identifier=?;'''
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

    return render_template('home.html')


@loginBP.route('/profile/<string:firstName>/<string:lastName>/<int:id>', methods=['GET', 'POST'])
def profile(firstName: str, lastName: str, id: int) -> str:
    if request.method == "GET":
        query = '''SELECT catchphrase, picture, job FROM Candidate WHERE id=?;'''
        arg = (id, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)

        dataList = cursor.fetchall()[0]
        
        db.close()

        data = {
            "catchphrase": dataList[0],
            "picture": f"/static/images/photos/{dataList[1]}",
            "job": dataList[2],
            "firstName": firstName,
            "lastName": lastName,
            "id": id
        }

        return render_template('profile.html', data=data)
    
    if request.method == "POST":
        catchphrase = request.form['catchphrase']
        pictureFile = request.files['picture']
        pictureName = pictureFile.filename

        if pictureName != "":
            save_candidate_picture(id, pictureName, "static/images/photos", pictureFile)


        query = '''UPDATE Candidate SET catchphrase=? WHERE id=?;'''
        args = (catchphrase, id)

        db, cursor = connectDatabase()
        cursor.execute(query, args)
        db.commit()
        db.close()

        return redirect(f"/profile/{firstName}/{lastName}/{id}")
