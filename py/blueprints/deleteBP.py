"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/12/2021
"""

# Import neded packages
from flask import Blueprint, redirect, request


# Import personnal modules
from py.database.connectDatabase import connectDatabase


# Definition of the blueprint
deleteBP = Blueprint('deleteBP', __name__)

@deleteBP.route('/delete/<string:dbTable>/<int:rowId>/<string:redirectPage>', methods=['GET', 'POST'])
def deleteRow(dbTable: str, rowId: int, redirectPage: str) -> str:
    if request.method == 'GET':
        redirectPage = "/" + redirectPage

        query = f"""DELETE FROM {dbTable} WHERE id=?;"""
        args = (rowId, )

        db, cursor = connectDatabase()
        cursor.execute(query, args)
        db.commit()
        db.close()

        return  redirect(redirectPage)