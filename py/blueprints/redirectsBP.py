"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from flask import Blueprint, redirect


# Import personnal modules
from py.database.connectDatabase import connectDatabase


# Definition of the blueprint
redirectsBP = Blueprint('redirectsBP', __name__)


@redirectsBP.route("/r/<string:mainPage>/<int:candidateID>")
def redirects_route(mainPage: str, candidateID: int) -> str:
    query = '''SELECT firstName, lastName FROM Candidate WHERE id=?;'''
    arg = (candidateID, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()[0]
    db.close()

    return redirect(f"/{mainPage}/{data[0]}/{data[1]}/{candidateID}")