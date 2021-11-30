"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint
from flask.templating import render_template


# Definition of the blueprint
mainBP = Blueprint('mainBP', __name__)


# Definition of the main route
@mainBP.route('/')
@mainBP.route('/home')
def home() -> str:
    return render_template('home.html')