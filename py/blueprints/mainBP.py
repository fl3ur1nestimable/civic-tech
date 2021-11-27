"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint
from flask.templating import render_template


# Definition of the blueprint
main = Blueprint('main', __name__)


# Definition of the main route
@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')