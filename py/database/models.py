"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask_login import UserMixin


# Import personal modules
from main import db

# Create various table for the db
## Creation of the Candidate table
class Candidate(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(30))
    lastName = db.Column(db.String(40))
    role = db.Column(db.Integer)
    password = db.Column(db.String(20))