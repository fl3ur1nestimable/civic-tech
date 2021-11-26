"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from werkzeug.security import generate_password_hash

# Import personal modules
from ..database.connectDatabase import connectDatabase
from ..core.getRole import *


# Starts the script with : python3 -i -m py.database.alterDatabase
def addCandidate(firstName: str, lastName: str, role: int, password: str) -> None:
    db, cursor = connectDatabase()

    researchQuery = '''SELECT * FROM user WHERE firstName=? and lastName=?;'''
    researchArgs = (firstName, lastName)
    cursor.execute(researchQuery, researchArgs)

    if len(cursor.fetchall()) == 0:
        researchQuery = '''SELECT * FROM user;'''
        cursor.execute(researchQuery)
        if len(cursor.fetchall()) == 0:
            addQuery = '''INSERT INTO user values (1, ?, ?, ?, ?);'''
            addArgs = (firstName, lastName, role, generate_password_hash(password, "sha256"))
        else:
            addQuery = '''INSERT INTO user values (?, ?, ?, ?);'''
            addArgs = (firstName, lastName, role, generate_password_hash(password, "sha256"))

        cursor.execute(addQuery, addArgs)
        db.commit()

        print(f"A new candidate has been added to the table with the informations :\n\
First Name : {firstName}\n\
Last Name : {lastName}\n\
Role : {getRole(role)}")

    else:
        print(f"A candidate with the first and last name entered already exist in table. Please enter another candidate")
    
    db.close()