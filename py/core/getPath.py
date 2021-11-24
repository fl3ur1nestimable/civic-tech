"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 24/11/2021
"""

# Import needed packages
from pathlib import Path


def get_path(i: int) -> str:
    """
        Function which send back the path of the first parents
        from the current forlder.

        Parameters :
            - i (integer) : index of the parent's path

        Returns :
            - cwd (string) : path of the i parent
    """

    cwd = Path(__file__).parents[i]
    cwd = str(cwd)
    return cwd