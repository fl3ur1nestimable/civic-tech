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
from python.core.coreJson import get_path, read_json


def test_get_path():
    test1 = 0
    result1 = '/Users/thibault/Documents/TN/PPII/project1-grp_e8/python/core'

    test2 = 3
    result2 = '/Users/thibault/Documents/TN/PPII'

    test3 = 1
    result3 = '/Users/thibault/Documents/TN/PPII/project1-grp_e8/python'

    assert type(get_path(test1)) is str

    assert get_path(test1) == result1
    assert get_path(test2) == result2
    assert get_path(test3) == result3



def test_read_json():
    test1 = "test1"
    result1 = {
        "test": "Bonjour"
    }

    test2 = "test2"
    result2 = {
        "test": {
            "Ceci est un test": 1
        }
    }

    assert type(read_json(test1)) is dict

    assert read_json(test1) == result1
    assert read_json(test2) == result2