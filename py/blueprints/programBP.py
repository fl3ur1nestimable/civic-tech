"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 27/11/2021
"""

# Import neded packages
from flask import Blueprint, session, request
from flask.helpers import flash
from flask.templating import render_template


# Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import checkValue
from py.core.truncatePrograms import truncatePrograms
from py.core.programAnalysis import rateDataWords


# Definition of the blueprint
programBP = Blueprint('programBP', __name__)


# Definition the program route
@programBP.route('/defineProgram', methods=['GET', 'POST'])
def define_program() -> str:
    if request.method == 'GET':
        userData = programBPUserData(session['id'])

        if checkValue('Candidate', 'id', session['id']):
            return render_template('referenceProgram.html', userData=userData)
        else:
            flash("Une erreur est survenue. Merci de réessayer.", "Red_flash")
            return render_template('home.html')
    
    elif request.method == 'POST':
        programContent = request.form['programmArea']
        memberContent= request.form['memberArea']

        insertProgram(session['id'], programContent)
        insertMembers(session['id'], memberContent)

        userData = programBPUserData(session['id'])

        flash("You have succesfully modified your program.", "Green_flash")
        return render_template('referenceProgram.html', userData=userData)
    
    else:
        return render_template('home.html')



@programBP.route('/programs')
def programsList() -> str:
    query = '''SELECT c.id, c.firstName, c.lastName, l.program FROM List AS l JOIN Candidate AS c ON l.id = c.listId'''
    db, cursor = connectDatabase()

    cursor.execute(query)
    data = cursor.fetchall()
    db.close()

    for i in range(len(data)):
        temp = [str(data[i][0]), data[i][1], data[i][2], truncatePrograms(data[i][3])]
        data[i] = temp
    
    return render_template('programsList.html', programsData=data)



# Definition of usefull functions for this BluePrint only

def programBPUserData(session_id: str) -> dict:
    """
        Functions to return the userData used in the program route in the program BP.

        Arguments:
            - session_id (string) : user's session id
        
        Returns :
            - userData (dict) : needed dict for the program page
    """
    db, cursor = connectDatabase()
    programContent = ""

    query = '''SELECT firstName, lastName FROM Candidate WHERE id=?;'''
    arg = (session_id, )

    cursor.execute(query, arg)
    for userTuple in cursor.fetchall():
        userFirstName = userTuple[0]
        userLastName = userTuple[1]
        
    query = '''SELECT l.program FROM List AS l JOIN Candidate AS c ON l.id = c.listId WHERE c.id=?;'''
    arg = (session_id, )

    cursor.execute(query, arg)
    for userTuple in cursor.fetchall():
        programContent = userTuple[0]
        
    db.close()

    userData = {
        'name': userFirstName+" "+userLastName,
        'program': programContent
    }

    return userData

def insertMembers(session_id:str, member: str)->None:
    requestQuery='''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session_id, )
    
    db, cursor = connectDatabase()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]

    insertQuery = ''''UPDATE Member SET firstName=?, lastName=?, job=? WHERE listId=?;'''
    insertArg = (member, listId)

    cursor.execute(insertQuery,insertArg)
    db.commit()
    cursor.close()
    db.close()


def insertProgram(session_id: int, program: str) -> None:
    topicsRate = rateDataWords(program)

    requestQuery = '''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session_id, )
    
    db, cursor = connectDatabase()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]

    print(listId)

    topicQuery = '''UPDATE ProgramGrade SET environment=?, social=?, economy=? WHERE listId=?;'''
    topicArgs = (topicsRate[0], topicsRate[1], topicsRate[2], listId)

    insertQuery = '''UPDATE List SET program=? WHERE id=?;'''
    insertArg = (program, listId)

    cursor.execute(insertQuery, insertArg)
    cursor.execute(topicQuery, topicArgs)

    db.commit()
    cursor.close()
    db.close()