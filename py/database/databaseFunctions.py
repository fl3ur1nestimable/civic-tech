"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 26/11/2021
"""

# Import needed modules
from typing import List



# Import personal modules
from .connectDatabase import connectDatabase
from py.core.programAnalysis import rateDataWords



def checkValue(table: str, field: str, value: str) -> bool:
    """
        Functions to check if a value (unique value not a tuple of values) is in given table

        Arguments:
            - table (string) : the table you want to search in
            - field (string) : the field in which the value is
            - value (string) : the searched value
        
        Returns :
            - retunBool (bool) : statements of the presence of the value in the table
    """

    if table == "List":
        query = '''SELECT * FROM List AS l JOIN Candidate AS c ON l.id=c.listId WHERE c.id=?;'''
        arg = (value, )

    else:
        query = '''SELECT * FROM ''' + table + ''' WHERE ''' + field + '''=?;'''
        arg = (value, )

    db, cursor = connectDatabase()

    cursor.execute(query, arg)
    returnBool = not cursor.fetchall() == []

    db.close()

    return returnBool


def getLastListId() -> int:
    """
        Function to get the last id of the List table

        Arguments :
            None
        
        Returns :
            - result (integer) : the max id in List Table
    """
    query = '''SELECT MAX(id) FROM List;'''

    db, cursor = connectDatabase()

    cursor.execute(query)
    result = cursor.fetchall()[0]
    db.close()

    return result


def check_user(userIp: str, listId: int) -> bool:
    """
        Functions to return whether or not a user is already in the users_vote database for a specific list

        Arguments :
            - userIp (string) : user's ip adress
            - listId (integer) : list's id
        
        Returns :
            - statement (boolean) : the needed statement
    """

    query = '''SELECT * FROM Users_vote WHERE userIP=? AND listId=?;'''
    arg = (userIp, listId)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    db.close()

    return len(data) != 0


def get_vote_office_to_json() -> List[dict]:
    query = '''SELECT lat, lon, name FROM Vote_office'''

    db, cursor = connectDatabase()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()

    my_list = []
    
    for elem in data:
        my_json = {}
        my_json['lat'] = elem[0]
        my_json['lon'] = elem[1]
        my_json['name'] = elem[2]
        my_list.append(my_json)

    return my_list


def count_vote(category: str, listId: int) -> int:
    query = f"""SELECT SUM({category}) FROM Users_vote WHERE listId=?;"""
    arg = (listId, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    db.close()

    return data[0][0]


def not_modified_program_grades(listId: int) -> bool:
    query = '''SELECT environment, social, economy FROM ProgramGrade WHERE listId=?;'''
    arg = (listId, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()[0]
    

    query = '''SELECT program FROM List WHERE id=?;'''
    cursor.execute(query, arg)
    program = cursor.fetchall()[0][0]
    db.close()

    programGrades = rateDataWords(program)

    data = list(data)
    
    return data == programGrades


def modify_program_grade(listId: int, voteTheme: str, modifySign= str) -> None:
    programGradesDict = {
        "economyVote": "economy",
        "socialVote": "social",
        "ecologyVote": "environment"
    }

    query = f"""SELECT {programGradesDict[voteTheme]} FROM ProgramGrade WHERE listId=?;"""
    arg = (listId, )

    modifyQuery = f"""UPDATE ProgramGrade SET {programGradesDict[voteTheme]}=? WHERE listId=?;"""

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()[0][0]

    modifyNumber = round(data + int(f"{modifySign}5"), 2)

    args = (modifyNumber, listId)

    cursor.execute(modifyQuery, args)
    db.commit()
    db.close()