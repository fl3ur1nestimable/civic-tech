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
from python.core.fileStorage import file_extension



def test_file_extension():
    test1 = "Bonjour"
    result1 = "Bonjour"

    test2 = "test.png"
    result2 = "png"

    test3 = "test.png.pdf"
    result3 = "pdf"

    assert type(file_extension(test1)) is str

    assert file_extension(test1) == result1
    assert file_extension(test2) == result2
    assert file_extension(test3) == result3