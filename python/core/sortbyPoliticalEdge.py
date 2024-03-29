"""
    Author : Guillot Thom
    Mail : thom.guillot@telecomnancy.eu
    Date : 30/11/2021
"""

# Import needed packages
from typing import List

def sortbyPoliticalEdge(L: list) -> List[list]:
    """
        Function to split candidates into their political edges category

        Parameters :
            - L (list) : A given list of candidates
        
        Returns :
            - Edges (List[list]) : A list of each list of candidates for every edges that exist
    """

    EG = ["Extrême-Gauche", "One"]
    G = ["Gauche", "Two"]
    C = ["Centre", "Three"]
    D = ["Droite", "Four"]
    ED = ["Extrême-Droite", "Five"]

    for k in range(len(L)):
        if L[k][13] == "Extreme-Gauche":
            EG.append(L[k])
        elif L[k][13] == "Gauche":
            G.append(L[k])
        elif L[k][13] == "Centre":
            C.append(L[k])
        elif L[k][13] == "Droite":
            D.append(L[k])
        elif L[k][13] == "Extreme-Droite":
            ED.append(L[k])
    
    Edges = [EG] + [G] + [C] + [D] + [ED]
    return Edges