"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

def getRole(role: int) -> str:
    roleStr = {
        "0": "Candidate",
        "1": "Administrator"
    }

    return roleStr[str(role)]