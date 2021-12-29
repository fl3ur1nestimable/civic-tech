"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 26/11/2021
"""

# Import needed packages
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import Tuple



def connectDatabase() -> Tuple[Connection, Cursor]:
    """
        Function that returns db connection and the cursor to interact with the database.db file

        Parameters :
            None

        Returns :
            - tuple [Connection, Cursor] : a tuple of the database connection and cursor
    """
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    return db, cursor