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
from ..core.generateConnectionLogs import generatePassword, generateIdentifier
from ..core.coreJson import read_json, write_json
from ..database.databaseFunctions import getLastListId



# Starts the script with : python3 -i -m py.database.alterDatabase
def addUser(firstName: str, lastName: str, email: str, job: str, politicalEdge: str) -> None:
    """
        Function to add a User in the users table of the database.db file. It also saves the loggins (identifier 
        and password in a json file : savedLoggin.json)

        Parameters :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - email (string) : email of the user
            - job (string) : job of the user
            - politicalEdge (string) : political edge of the list of the user

        Returns :
            None
        
        Prints :
            - firstName (string) : first name of the candidate
            - lastName (string) : last name of the candidate
            - email (string) : email of the user
            - identifier (string) : 6-digits identifier for the user
            - password (string) : 20-characters password of the user
     
    """
    # Preconditions
    assert type(firstName) is str
    assert type(lastName) is str
    assert type(email) is str
    assert type(job) is str
    assert type(politicalEdge) is str
    assert job in ["agriexp" ,"artcomchef" ,"cadreprofintsup" ,"profintermed" ,"employe" ,"ouvrier" ,"retraite" ,"sansactprof"]
    assert politicalEdge in ["Extreme-Gauche", "Gauche", "Centre", "Droite", "Extreme-Droite"]

    db, cursor = connectDatabase()

    researchQuery = '''SELECT * FROM Candidate WHERE firstName = ? and lastName = ?;'''
    researchArgs = (firstName, lastName)
    cursor.execute(researchQuery, researchArgs)

    if len(cursor.fetchall()) == 0:
        identifier = generateIdentifier(6)
        password = generatePassword(20)

        listQuery = '''INSERT INTO List (program, politicalEdge) values (?, ?);'''
        listArg = ("", politicalEdge)

        listId = getLastListId()[0]

        if listId is None:
            listId = 1
        else:
            listId += 1

        addQuery = '''INSERT INTO Candidate (firstName, lastName, email, job, listId, identifier, password) VALUES (?, ?, ?, ?, ?, ?, ?);'''
        addArgs = (firstName, lastName, email, job, listId, identifier, generate_password_hash(password, "sha256"))

        programQuery = '''INSERT INTO ProgramGrade (listId, environment, social, economy) VALUES (?, ?, ?, ?);'''
        programArgs = (listId, 0, 0, 0)

        memberQuery = '''INSERT INTO jobMemberGrade (listId, agriexp, artcomchef, cadreprofintsup, profintermed, employe, ouvrier, retraite, sansactprof) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        memberArgs = (listId, 0, 0, 0, 0, 0, 0, 0, 0)


        try:
            cursor.execute(addQuery, addArgs)
            cursor.execute(listQuery, listArg)
            cursor.execute(programQuery, programArgs)
            cursor.execute(memberQuery,memberArgs)

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


def addVote_office(lat: int, lon: int, name: str) -> None:
    """
        Function to add a Vote_office in the vote_office table of the database.db file.

        Parameters :
            - lat (integer) : latitude of the vote office
            - lon (integer) : longitude of the vote office
            - name (string) : name of  the vote office

        Returns :
            None
     
    """
    
    query = '''INSERT INTO Vote_office (lat, lon, name) VALUES (?, ?, ?);'''
    args = (lat, lon, name)
    
    db, cursor = connectDatabase()
    cursor.execute(query, args)
    db.commit()
    db.close()


def addVote(listId: int, userIp: str) -> None:
    """
        Function to add 299 votes in every topics of a list. 

        Parameters :
            - listId (integer) : the id of the list to alter vote

        Returns :
            None
     
    """

    query = '''INSERT INTO Users_vote (listId, userIP, economyVote, ecologyVote, socialVote) VALUES (?, ?, 299, 299, 299);'''
    args = (listId, userIp)

    db, cursor = connectDatabase()
    cursor.execute(query, args)
    db.commit()
    db.close()
