"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 22/12/2021
"""

# Import needed modules
import string
import random
import os

# Import personal modules
from py.database.connectDatabase import connectDatabase


def file_extension(fileName: str) -> str:
    return fileName.split('.')[-1]


def generate_unique_filename(length: int, fileExtension: str) -> str:
    query = '''SELECT * FROM Candidate WHERE picture=?;'''

    alphabet = string.ascii_letters + string.digits 
    code =''.join(random.choice(alphabet)for i in range(length))

    arg = (code + '.' + fileExtension, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    db.close()

    if len(data) == 0:
        return code
    else:
        return generate_unique_filename(length, fileExtension)



def save_candidate_picture(candidateID: int, fileName: str, picturePath: str, file) -> None:
    fileExtension = file_extension(fileName)

    uniqueCode = generate_unique_filename(6, fileExtension)
    uniqueCode += "." + fileExtension

    file.save(os.path.join(picturePath, uniqueCode))

    removeQuery = '''SELECT picture FROM Candidate WHERE id=?;'''
    removeArg = (candidateID, )
    
    addQuery = "UPDATE Candidate SET picture=? WHERE id=?;"
    addArgs = (uniqueCode, candidateID)

    db, cursor = connectDatabase()
    cursor.execute(removeQuery, removeArg)
    data = cursor.fetchall()

    if data[0][0] is not None:
        os.remove(os.path.join(picturePath, data[0][0]))
    
    cursor.execute(addQuery, addArgs)
    db.commit()
    db.close()