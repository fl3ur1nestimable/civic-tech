"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 03/11/2021
"""

# Import personal modules
from python.database.connectDatabase import connectDatabase
from python.core.coreJson import write_json
from python.database.alterDatabase import addUser, addVote_office


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
    DROP TABLE IF EXISTS Users_vote;
    DROP TABLE IF EXISTS Vote_office;
    DROP TABLE IF EXISTS jobMemberGrade;

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
    );

    CREATE TABLE Users_vote
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        listId INTEGER,
        userIP TEXT NOT NULL,
        economyVote INTEGER DEFAULT 0,
        ecologyVote INTEGER DEFAULT 0,
        socialVote INTEGER DEFAULT 0,
        FOREIGN KEY (listId) REFERENCES List(id)
    );

    CREATE TABLE Vote_office
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lat FLOAT NOT NULL,
        lon FLOAT NOT NULL,
        name TEXT NOT NULL
    );

    CREATE TABLE jobMemberGrade
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        listId INTEGER NOT NULL,
        agriexp INTEGER DEFAULT 0,
        artcomchef INTEGER DEFAULT 0,
        cadreprofintsup INTEGER DEFAULT 0,
        profintermed INTEGER DEFAULT 0,
        employe INTEGER DEFAULT 0,
        ouvrier INTEGER DEFAULT 0,
        retraite INTEGER DEFAULT 0,
        sansactprof INTEGER DEFAULT 0,
        FOREIGN KEY (listId) REFERENCES List(id)
    )
    '''

    cursor.executescript(query)
    db.commit()
    db.close()

    addUser('Thibault', 'Cheneviere', 'thibault.cheneviere@telecomnancy.eu', 'cadreprofintsup', 'Droite')
    addUser('Elion', 'Hashani', 'elion.hashani@telecomnancy.eu', 'artcomchef', 'Extreme-Gauche')

    addVote_office(48.693853844446295, 6.183311422401857, "Place Stanislas")
    addVote_office(48.690021148491276, 6.176367075585757, "Fnac Nancy")
    addVote_office(48.68621583435226, 6.171759792647458, "Le Chat Noir")