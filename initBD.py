"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 03/11/2021
"""

# Import personal modules
from py.database.connectDatabase import connectDatabase
from py.core.coreJson import write_json


if __name__ == "__main__":
    # Reset the savedLoggin.json file
    data = {}
    write_json(data, 'savedLoggin')

    db, cursor = connectDatabase()
    
    # Script for the database
    query = '''
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS programs;

    CREATE TABLE users 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, email TEXT, role INTEGER, identifier TEXT UNIQUE, password TEXT);

    CREATE TABLE programs
    (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, content TEXT, FOREIGN KEY (user_id) REFERENCES users(id));
    '''

    cursor.executescript(query)
    db.commit()
    db.close()