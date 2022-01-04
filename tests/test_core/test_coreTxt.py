"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 04/01/2021
"""

# Import needed modules
import pathlib, sys

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from python.core.coreTxt import open_txt


def test_open_txt():
    test1 = "test1"
    result1 = "Bonjour ceci est un test !"

    test2 = "test2"
    result2 = "Elion est un candidat d'Extreme-Gauche !\nCeci est un test 2."

    assert type(open_txt(test1)) is str

    assert open_txt(test1) == result1
    assert open_txt(test2) == result2