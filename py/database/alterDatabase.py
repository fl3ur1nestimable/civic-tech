"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import neded packages
from werkzeug.security import generate_password_hash

# Import personal modules
from main import db
from models import Candidate
from core import getRole


def addCandidate(firstName: str, lastName: str, role: int, password: str) -> None:
    candidate = Candidate.query.filter_by(firstName=firstName, lastName=lastName).first()
    if candidate is None:
        hashedPassword = generate_password_hash(password, method='sha256')
        newCandidate = Candidate(firstName=firstName, lastName=lastName, role=role, password=hashedPassword)

        db.session.add(newCandidate)
        db.session.commit()

        print(f"A new candidate has been added to the table with the informations :\n\
First Name : {firstName}\n\
Last Name : {lastName}\n\
Role : {getRole(role)}")

    else:
        print(f"A candidate with the first and last name entered already exist in table. Please enter another candidate")
    
    return