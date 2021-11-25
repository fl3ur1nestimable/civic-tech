"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 03/11/2021
"""

# Import personal modules
from main import db, create_app
from py.database.models import *

if __name__ == "__main__":
    db.create_all(app=create_app())