"""
    Author : Cheneviere Thibault & Hashani Elion
    Mail : thibault.cheneviere@telecomnancy.eu & elion.hashani@telecomnancy.eu
    Date : 27/11/2021 & 17/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request, redirect
from flask.helpers import flash
from flask.scaffold import F
from flask.templating import render_template


# Import personal modules
from python.database.connectDatabase import connectDatabase
from python.database.databaseFunctions import checkValue
from python.core.truncatePrograms import truncatePrograms
from python.core.programAnalysis import rateDataWords
from python.core.memberAnalysis import rateList


# Definition of the blueprint
programBP = Blueprint('programBP', __name__)


# Definition the program route
@programBP.route('/defineProgram', methods=['GET', 'POST'])
def define_program() -> str:
    requestQuery='''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session['id'], )
                
    db, cursor = connectDatabase()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]
    userData = programBPUserData(session['id'])
    query='''SELECT * FROM Member WHERE listId=?;'''
    arg=(listId,)
    cursor.execute(query,arg)
    data = cursor.fetchall()
    
    if request.method == 'GET':
        rateList(listId)
        if checkValue('Candidate', 'id', session['id']):
            return render_template('referenceProgram.html', userData=userData,data=data)
        
        else:
            flash("Une erreur est survenue. Merci de réessayer.", "Red_flash")
            return render_template('home.html')

    elif request.method == 'POST':
        if request.form.get('Publier') == "Publier" :
            programContent = request.form['programmArea']
        
            insertProgram(session['id'], programContent)
        
            userData = programBPUserData(session['id'])

            db.close()

            flash("You have succesfully modified your program.", "Green_flash")
            return render_template('referenceProgram.html', userData=userData, data=data)
            
        else:
            lastnameMember = request.form.get('lastnameMember')
            firstnameMember = request.form.get('firstnameMember')
            jobMember = request.form.get("jobMember")
            userData = programBPUserData(session['id'])

            if lastnameMember == "" or firstnameMember == "" or not jobMember:
                db.close()
                
                flash("Information(s) manquante(s)", "Red_flash")
                return render_template('referenceProgram.html', userData=userData, data=data)

            elif not CheckMember(firstnameMember,lastnameMember,listId,jobMember):
                db.close()
                flash("Membre déjà présent", "Red_flash")
                print('oui')
                return render_template('referenceProgram.html',userData=userData,data=data)

            else:

                insertQuery = '''INSERT INTO Member (firstName, lastName, listId, job) VALUES (?, ?, ?, ?);'''
                insertArg = (firstnameMember,lastnameMember,listId,jobMember)

                cursor.execute(insertQuery,insertArg)
                db.commit()
                requestQuery='''SELECT listId FROM Candidate WHERE id=?;'''
                arg = (session['id'], )

                cursor.execute(requestQuery, arg)
                listId = cursor.fetchall()[0][0]
                userData = programBPUserData(session['id'])
                query='''SELECT lastName, firstName, job FROM Member WHERE listId=?;'''
                arg=(listId,)
                cursor.execute(query,arg)
                data=cursor.fetchall()

                rateList(listId)

                cursor.close()
                db.close()

                flash("You have succesfully added a new member.", "Green_flash")
                return redirect('/defineProgram')
    else:
        return render_template('home.html')



@programBP.route('/programs')
def programsList() -> str:
    query = '''SELECT c.firstName, c.lastName, l.program ,c.id FROM List AS l JOIN Candidate AS c ON l.id = c.listId'''
    db, cursor = connectDatabase()

    cursor.execute(query)
    data = cursor.fetchall()
    db.close()



    for i in range(len(data)):
        temp = [data[i][0], data[i][1], truncatePrograms(data[i][2]), str(data[i][3])]
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

def CheckMember(fname: str, lname: str, listid: int, job: str) -> bool:
    checkQuery='''SELECT * FROM Member WHERE firstName=? AND lastName=? AND listId=? AND job=?'''
    checkArg=(fname,lname,listid,job)
    db,cursor=connectDatabase()
    cursor.execute(checkQuery,checkArg)
    result=cursor.fetchall()
    db.close()
    
    return (len(result) == 0)

def insertProgram(session_id: int, program: str) -> None:
    topicsRate = rateDataWords(program)

    requestQuery = '''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session_id, )
    
    db, cursor = connectDatabase()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]

    topicQuery = '''UPDATE ProgramGrade SET environment=?, social=?, economy=? WHERE listId=?;'''
    topicArgs = (topicsRate[0], topicsRate[1], topicsRate[2], listId)

    insertQuery = '''UPDATE List SET program=? WHERE id=?;'''
    insertArg = (program, listId)

    cursor.execute(insertQuery, insertArg)
    cursor.execute(topicQuery, topicArgs)

    db.commit()
    cursor.close()
    db.close()

