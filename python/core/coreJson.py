"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 27/11/2021
"""

# Import needed packages
import json
from pathlib import Path



def get_path(i: int) -> str:
    """
        Function which send back the path of the i parent from the current forlder.

        Parameters :
            - i (integer) : index of the parent's path

        Returns :
            - cwd (string) : path of the i parent
    """

    cwd = Path(__file__).parents[i]
    cwd = str(cwd)
    return cwd


def read_json(filename: str) -> dict:
    """
        Function to read a json file

        Parameters :
            - filename (string) : filename
        
        Returns :
            - data (dict) : data stored in the json file
    """

    cwd = get_path(2)
    with open(cwd+'/json/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data: dict, filename: str) -> None:
    """
        Function to modify a json file.

        Parameters :
            - data (dict) : modification of the json file
            - filename (string) : name of the json file to modify
        
        Returns :
            None
    """

    cwd = get_path(2)

    with open(cwd+'/json/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)