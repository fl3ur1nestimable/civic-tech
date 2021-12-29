"""
    Author : Antoine Yebouet
    Mail : antoine.yebouet@telecomnancy.eu
    Date : 06/12/2021
"""

# Import neded packages
from flask import Blueprint, session, request, flash, render_template, redirect


#Import personal modules
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import check_user, count_vote, modify_program_grade, not_modified_program_grades


#Definition of the blueprint
progFullBP = Blueprint('progFullBP',__name__)


@progFullBP.route('/program/<string:firstName>/<string:lastName>/<int:id>', methods=['GET', 'POST'])
def program(firstName: str, lastName: str, id: int) -> str:
    if request.method == 'GET':
        query = '''SELECT l.program, c.listId, c.catchphrase,c.picture FROM Candidate AS c JOIN List AS l ON c.listId=l.id WHERE c.id=?;'''
        arg = (id, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)

        data=cursor.fetchall()

        prog = data[0][0]
        listId = data[0][1]
        citation=data[0][2]
        photo=data[0][3]

        query2='''SELECT g.environment,g.social,g.economy FROM ProgramGrade as g WHERE g.listId=? '''
        arg2=(listId, )
        cursor.execute(query2,arg2)
        data2=cursor.fetchall()
        grades=[data2[0][0],data2[0][1],data2[0][2]]

        query3='''SELECT m.firstName,m.lastName,m.job FROM Member as m WHERE m.listID =?'''
        cursor.execute(query3,arg2)
        liste_membres=cursor.fetchall()

        if check_user(request.remote_addr, listId):
            query4 = '''SELECT economyVote, ecologyVote, socialVote FROM Users_vote WHERE userIp=? AND listId=?;'''
            args4 = (request.remote_addr, listId)
            cursor.execute(query4, args4)
            data4 = cursor.fetchall()[0]
            print(data4)
        else:
            data4 = (0, 0, 0)
        db.close()

        candidateDict = {
            "id": id,
            "listId": listId,
            "firstName": firstName,
            "lastName": lastName,
            "program": prog,
            "grades": grades,
            "catchphrase": citation,
            "membres": liste_membres,
            "picture": f"{photo}"
        }

        voteDict = {
            "ecology": str(data4[1]),
            "economy": str(data4[0]),
            "social": str(data4[2])
        }

        return render_template('program.html', data=candidateDict, voteData=voteDict)


@progFullBP.route('/vote/<string:voteTheme>/<string:addSign>/<int:listId>/<string:programRoute>', methods=['GET', 'POST'])
def voteRoute(voteTheme: str, addSign: str, listId: int, programRoute: str) -> str:
    if request.method == 'GET':
        dataRoute = programRoute.split('--')
        
        programRoute = ""
        for i in dataRoute:
            programRoute += "/" + i
        
        voteTheme += "Vote"
        user_ip = request.remote_addr

        db, cursor = connectDatabase()

        if not check_user(user_ip, listId):
            query = f"""INSERT INTO Users_vote (listId, userIP, {voteTheme}) VALUES (?, ?, {addSign}1);"""
            args = (listId, user_ip)

            voteCount = count_vote(voteTheme, listId)

            if voteCount == 300 and not_modified_program_grades(listId):
                modify_program_grade(listId, voteTheme, "+")
            elif voteCount == -300 and not_modified_program_grades(listId):
                modify_program_grade(listId, voteTheme, "-")
        else:
            query = f"""UPDATE Users_vote SET {voteTheme}=? WHERE listId=? AND userIP=?;"""
            args = (addSign+'1', listId, user_ip)
        
        cursor.execute(query, args)
        db.commit()
        db.close()

        flash("You have successfuly voted.", "Green_flash")
        return redirect(programRoute)
