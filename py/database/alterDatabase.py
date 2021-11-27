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
from ..core.getRole import getRole
from ..core.generateConectionLogs import generatePassword, generateIdentifier
from ..core.coreJson import read_json, write_json



# Starts the script with : python3 -i -m py.database.alterDatabase
def addUser(firstName: str, lastName: str, role: int, email: str) -> None:
    """
        Function to add a User in the users table of the database.db file. It also saves the loggins (identifier 
        and password in a json file : savedLoggin.json)

        Parameters :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - role (integer) : integer value of the user's role. Refet to the getRole.py file to see the roles
            - email (string) : email of the user

        Returns :
            None
        
        Prints :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - email (string) : email of the user
            - identifier (string) : 6-digits identifier for the user
            - password (string) : 20-characters password of the user
            - role (integer) : integer value of the user's role. Refet to the getRole.py file to see the roles
            
    """
    db, cursor = connectDatabase()

    researchQuery = '''SELECT * FROM users WHERE firstName = ? and lastName = ?;'''
    researchArgs = (firstName, lastName)
    cursor.execute(researchQuery, researchArgs)

    if len(cursor.fetchall()) == 0:
        identifier = generateIdentifier(6)
        password = generatePassword(20)

        addQuery = '''INSERT INTO users(firstName, lastName, email, role, identifier, password) values (?, ?, ?, ?, ?, ?);'''
        addArgs = (firstName, lastName, email, role, identifier, generate_password_hash(password, "sha256"))

        try:
            cursor.execute(addQuery, addArgs)
            db.commit()
        except IntegrityError:
            return addUser(firstName, lastName, role, email)

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
Password : {password}\n\
Role : {getRole(role)}")

    else:
        print(f"A candidate with the first and last name entered already exist in table. Please enter another candidate")
    
    db.close()