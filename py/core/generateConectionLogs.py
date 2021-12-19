"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 26/11/2021
"""

# Import needed packages
from random import randint, choice
from string import ascii_letters, digits


# Import personal packages


def generateIdentifier(nbChr: int) -> str:
    """
        Function that returns a randomly generated digit identifier

        Parameters :
            - nbChr (integer) : number of  characters needed in the identifier string

        Returns :
            - indentifier (string) : randomly generated identifier with only digits
    """
    identifier = ""

    for i in range(nbChr):
        identifier += str(randint(0,9))

    return identifier


def generatePassword(nbChr: int) -> str:
    """
        Function that returns a randomly generated password. The password can contain
        every printable characters.

        Parameters :
            - nbChr (integer) : number of  characters needed in the password string

        Returns :
            - password (string) : randomly generated password
    """
    password = ""
    stringsAvailable = [ascii_letters, digits]
    for i in range(nbChr):
        password += choice(choice(stringsAvailable))
    
    return password


if __name__ == "__main__":
    pass