"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from werkzeug.security import generate_password_hash
from sqlite3 import IntegrityError


# Import personal modules
from ..database.connectDatabase import connectDatabase
from ..core.generateConectionLogs import generatePassword, generateIdentifier
from ..core.coreJson import read_json, write_json
from ..database.databaseFunctions import getLastListId



# Starts the script with : python3 -i -m py.database.alterDatabase
def addUser(firstName: str, lastName: str, email: str) -> None:
    """
        Function to add a User in the users table of the database.db file. It also saves the loggins (identifier 
        and password in a json file : savedLoggin.json)

        Parameters :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - email (string) : email of the user

        Returns :
            None
        
        Prints :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - email (string) : email of the user
            - identifier (string) : 6-digits identifier for the user
            - password (string) : 20-characters password of the user
     
    """
    db, cursor = connectDatabase()

    researchQuery = '''SELECT * FROM Candidate WHERE firstName = ? and lastName = ?;'''
    researchArgs = (firstName, lastName)
    cursor.execute(researchQuery, researchArgs)

    if len(cursor.fetchall()) == 0:
        identifier = generateIdentifier(6)
        password = generatePassword(20)

        listQuery = '''INSERT INTO List (program) values (?);'''
        listArg = ("", )

        listId = getLastListId()[0]
        print(listId)

        if listId is None:
            listId = 1
        else:
            listId += 1

        addQuery = '''INSERT INTO Candidate (firstName, lastName, email, listId, identifier, password) values (?, ?, ?, ?, ?, ?);'''
        addArgs = (firstName, lastName, email, listId, identifier, generate_password_hash(password, "sha256"))

        try:
            cursor.execute(addQuery, addArgs)
            db.commit()

            cursor.execute(listQuery, listArg)
            db.commit()
        except IntegrityError:
            return addUser(firstName, lastName, email)

        # Save the loggin data in the json file savedLoggin.json
        data = read_json('savedLoggin')
        data[firstName+" "+lastName] = {}
        data[firstName+" "+lastName]['identifier'] = identifier
        data[firstName+" "+lastName]['password'] = password
        write_json(data, 'savedLoggin')
        
        print(f"A new candidate has been added to the table with the informations :\n\
First Name : {firstName}\n\
Last Name : {lastName}\n\
Email : {email}\n\
Identifier : {identifier}\n\
Password : {password}\n")

    else:
        print(f"A candidate with the first and last name entered already exist in table. Please enter another candidate")
    
    db.close()