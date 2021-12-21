"""
    Author : Antoine Yebouet
    Mail : antoine.yebouet@telecomnancy.eu
    Date : 06/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request
from flask.helpers import flash
from flask.templating import render_template


#Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import checkValue
from py.core.truncatePrograms import truncatePrograms

#Definition of the blueprint
progFullBP = Blueprint('progFullBP',__name__)


@progFullBP.route('/program/<string:firstName>/<string:lastName>/<int:id>')
def program(firstName: str, lastName: str, id: int) -> str:
    query = '''SELECT l.program, c.listId, c.catchphrase,c.picture FROM Candidate AS c JOIN List AS l ON c.listId=l.id WHERE c.id=?;'''
    arg = (id, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)

    data=cursor.fetchall()

    prog = data[0][0]
    listId = data[0][1]
    citation=data[0][2]
    photo=data[0][3]

    db.close()

    query2='''SELECT g.environment,g.social,g.economy FROM ProgramGrade as g WHERE g.listId=? '''
    arg2=(listId, )
    db2, cursor2 = connectDatabase()
    cursor2.execute(query2,arg2)
    data2=cursor2.fetchall()
    grades=[data2[0][0],data2[0][1],data2[0][2]]
    db2.close()

    query3='''SELECT m.firstName,m.lastName,m.job FROM Member as m WHERE m.listID =?'''
    db3, cursor3 =connectDatabase()
    cursor3.execute(query3,arg2)
    liste_membres=cursor3.fetchall()
    db3.close()

    return render_template('program.html',nomCandidat=firstName,prenomCandidat=lastName,prog=prog,grades=grades,citation=citation,membres=liste_membres,photo=photo)