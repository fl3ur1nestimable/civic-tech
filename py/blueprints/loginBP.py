"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint, request
from flask.templating import render_template


# Definition of the blueprint
login = Blueprint('login', __name__)


# Definition of the route
@login.route('/login')
def login_route():
    return render_template('login.html')


@login.route('/login', methods=['GET', 'POST'])
def login_validation():
    identifier = request.form['identifier']
    password = request.form['password']

    return render_template('login.html')