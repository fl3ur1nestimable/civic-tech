"""
    Author : Hashani Elion
    Mail : elion.hashani@telecomnancy.eu
    Date : 02/01/2022
"""

# Import needed modules
import pathlib, sys, os, pytest

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)

# Import personal module
from python.core.truncatePrograms import truncatePrograms

def test_truncatePrograms():
    program1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec odio est, cursus consequat accumsan mollis, ornare a magna. Donec pretium, ante non porttitor semper, augue."
    ## len(program1) = 25 ##
    result1 = program1+" "

    assert truncatePrograms(program1) == result1

    program2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus at leo suscipit elementum. Duis quis sem efficitur, ultrices ex eget, cursus tellus. Donec ut enim massa. Nunc ullamcorper dignissim magna, quis lobortis justo mollis ut. Suspendisse quis orci at nibh."
    ## len(program2) = 41 ##
    result2 = ' '.join(program2.split(" ")[:-1]) + "  ..."

    assert truncatePrograms(program2) == result2

    program3 = ""
    ## len(program3) = 0 ##
    result3 = " "

    assert truncatePrograms(program3) == result3

    program4 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec maximus at leo suscipit elementum. Duis quis sem efficitur, ultrices ex eget, cursus tellus. Donec ut enim massa. Nunc ullamcorper dignissim magna, quis lobortis justo mollis ut. Suspendisse quis orci at."
    ## len(program4) = 40 ##
    result4 = program4 + " "

    assert truncatePrograms(program4) == result4

    with pytest.raises(AttributeError): ## AttributeError: 'list' object has no attribute 'split' ##
        program5 = ["oui","non"]
        truncatePrograms(program5)