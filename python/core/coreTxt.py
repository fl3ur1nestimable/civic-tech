"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 01/12/2021
"""


# Import needed modules


# Import personal modules
from python.core.coreJson import get_path


def open_txt(filename: str) -> str:
    cwd = get_path(2)
    filePath = cwd + "/data/txt/" + filename + ".txt"

    with open(filePath, 'r') as file:
        data = file.read()
    
    return data