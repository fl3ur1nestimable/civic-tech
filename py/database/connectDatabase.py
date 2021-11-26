"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 26/11/2021
"""

# Import neded packages
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor



def connectDatabase() -> tuple[Connection, Cursor]:
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    return db, cursor