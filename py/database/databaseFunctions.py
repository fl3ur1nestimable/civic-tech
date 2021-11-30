"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 26/11/2021
"""


# Import personal modules
from typing import List, Tuple
from .connectDatabase import connectDatabase



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

    query = '''SELECT * FROM ''' + table + ''' WHERE ''' + field + '''=?;'''
    arg = (value, )

    db, cursor = connectDatabase()

    cursor.execute(query, arg)
    returnBool = not cursor.fetchall() == []

    db.close()

    return returnBool