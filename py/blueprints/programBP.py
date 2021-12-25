"""
    Author : Cheneviere Thibault & Hashani Elion
    Mail : thibault.cheneviere@telecomnancy.eu & elion.hashani@telecomnancy.eu
    Date : 27/11/2021 & 17/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request, redirect, flash, render_template


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
        query='''SELECT lastName, firstName, job, id FROM Member;'''
        db,cursor=connectDatabase()
        cursor.execute(query)
        data=cursor.fetchall()
        db.close()
        

        if checkValue('Candidate', 'id', session['id']):
            return render_template('referenceProgram.html', userData=userData,data=data)
        
        else:
            flash("Une erreur est survenue. Merci de réessayer.", "Red_flash")
            return render_template('home.html')
    
    elif request.method == 'POST':
        userData = programBPUserData(session['id'])
        query='''SELECT lastName, firstName, job, id FROM Member;'''
        db,cursor=connectDatabase()
        cursor.execute(query)
        data=cursor.fetchall()
        db.close()
        print(data)

        if request.form.get('Publier') == "Publier" :
            programContent = request.form['programmArea']
        
            insertProgram(session['id'], programContent)
        
            userData = programBPUserData(session['id'])

            flash("You have succesfully modified your program.", "Green_flash")
            return render_template('referenceProgram.html', userData=userData,data=data)
        
        elif request.form.get('Retirer') is int:
            a=request.form.get('Retirer')
            print(a)
            db, cursor = connectDatabase()
            
            query = '''DELETE FROM Member WHERE id=?;'''
            arg = (a,)

            
            cursor.execute(query, arg)
            db.commit()
            db.close()
            flash("You have successfully deleted a member from your list !", "Green_flash")
            return render_template('referenceProgram.html', userData=userData,data=data)
            

        else:
            lastnameMember = request.form.get('lastnameMember')
            firstnameMember = request.form.get('firstnameMember')
            jobMember = request.form.get("jobMember")
            userData = programBPUserData(session['id'])

            if lastnameMember == "" or firstnameMember == "" or not jobMember:
                
                flash("Information(s) manquante(s)", "Red_flash")
                return render_template('referenceProgram.html', userData=userData, data=data)

            elif lastnameMember and firstnameMember and jobMember in db:
                flash("Membre déjà inclus", "Red_flash")
                return render_template('referenceProgram.html',userData=userData,data=data)

            else:
                requestQuery='''SELECT listId FROM Candidate WHERE id=?;'''
                arg = (session['id'], )
                
                db, cursor = connectDatabase()

                cursor.execute(requestQuery, arg)
                listId = cursor.fetchall()[0][0]

                insertQuery = '''INSERT INTO Member (firstName, lastName, listId, job) VALUES (?, ?, ?, ?);'''
                insertArg = (firstnameMember,lastnameMember,listId,jobMember)

                cursor.execute(insertQuery,insertArg)
                db.commit()
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

def checkMember(session_id: int,firstname:str,lastname:str,job:str)->bool:
    requestQuery = '''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session_id, )
    
    db, cursor = connectDatabase()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]
    db,cursor=connectDatabase()
    checkQuery='''SELECT * FROM Member WHERE firstName=? AND lastName=? AND listId=? AND job=?;'''
    checkArg=(firstname,lastname,listId,job)
    cursor.execute(checkQuery,checkArg)
    result=cursor.fetchall()
    db.commit()
    db.close()
    return (len(result)==0)


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
