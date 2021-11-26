"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 03/11/2021
"""

# Import personal modules
from py.database.connectDatabase import connectDatabase


if __name__ == "__main__":
    db, cursor = connectDatabase()
    
    query = '''
    DROP TABLE IF EXISTS user;

    CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, role INTEGER, password TEXT);
    '''

    cursor.executescript(query)
    db.commit()
    db.close()