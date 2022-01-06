"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 03/11/2021
"""

# Import personal modules
from python.database.connectDatabase import connectDatabase
from python.core.coreJson import write_json
from python.database.alterDatabase import addMinusVote, addUser, addVote, addVote_office


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

    addVote_office(48.69309516830485, 6.183608649043081, "Hotel de ville")
    addVote_office(48.691447643686786, 6.178480537706399, "Lycée Henri-Poincaré")
    addVote_office(48.7004406746501, 6.185580801981988, "Gymnase Maurice Jacquet")
    addVote_office(48.700734872665045, 6.171515037772073, "Ecole maternelle Alfred Mézières")
    addVote_office(48.70053125310194, 6.176203051861037, "Gymnase Charles V")
    addVote_office(48.69005103062423, 6.196344188137936, "Gymnase Martiny")
    addVote_office(48.68885275314536, 6.160189933906852, "Centre Santifontaine")
    addVote_office(48.69280778716376, 6.148765676274994, "Ecole maternelle Buthegnemont")
    addVote_office(48.70178677444582, 6.153946434086223, "Gymnase Buffon")
    addVote_office(48.679933462057534, 6.16284048347884, "Gymnase Chopin")

    addVote(1, "107.61.67.119")
    addMinusVote(2, "20.96.249.185")