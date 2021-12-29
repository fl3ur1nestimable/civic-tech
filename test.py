"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 29/12/2021
"""

# Import personal modules
from py.database.databaseFunctions import count_vote, not_modified_program_grades
from py.database.connectDatabase import connectDatabase
from py.database.databaseFunctions import modify_program_grade
from py.core.programAnalysis import rateDataWords

# print(count_vote("economyVote", 1))
# print(not_modified_program_grades(1))

def reset_program():
    query = '''SELECT program FROM List WHERE id=1;'''
    db, cursor = connectDatabase()
    cursor.execute(query)
    program = cursor.fetchall()[0][0]
    
    query = """UPDATE ProgramGrade SET environment=?, economy=?, social=? WHERE listId=?;"""
    data = rateDataWords(program)
    args = (data[0], data[1], data[2], 1)

    cursor.execute(query, args)
    db.commit()
    db.close()


# reset_program()
# modify_program_grade(1, "ecologyVote", "+")