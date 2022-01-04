"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 04/01/2021
"""

# Import needed modules
import pathlib, sys
from string import ascii_letters, digits

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from python.core.generateConnectionLogs import generateIdentifier, generatePassword


def test_generateIdentifier():
    test1 = 0
    result1 = ""

    test2 = 6

    assert type(generateIdentifier(test1)) is str
    assert generateIdentifier(test1) == result1

    assert type(generateIdentifier(test2)) is str
    assert len(generateIdentifier(test2)) == 6
    
    for i in generateIdentifier(test2):
        assert i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def test_generatePassword():
    test1 = 0
    result1 = ""

    test2 = 6

    assert type(generatePassword(test1)) is str
    assert generatePassword(test1) == result1

    assert type(generatePassword(test2)) is str

    for i in generatePassword(test2):
        assert i in ascii_letters or i in digits