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
    DROP TABLE IF EXISTS Candidate;
    DROP TABLE IF EXISTS List;
    DROP TABLE IF EXISTS ProgramGrade;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE Candidate
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        picture TEXT,
        catchphrase TEXT,
        listId INTEGER,
        email TEXT UNIQUE,
        job TEXT,
        identifier TEXT UNIQUE,
        password TEXT,
        FOREIGN KEY (listId) REFERENCES List(id)
    );

    CREATE TABLE List
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        program TEXT,
        politicalEdge TEXT
    );

    CREATE TABLE ProgramGrade
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        listId INTEGER,
        environment FLOAT,
        social FLOAT,
        economy FLOAT,
        FOREIGN KEY (listId) REFERENCES List(id)
    );

    CREATE TABLE Member
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        listId INTEGER,
        job TEXT,
        FOREIGN KEY (listId) REFERENCES List(id)
    )
    '''

    cursor.executescript(query)
    db.commit()
    db.close()