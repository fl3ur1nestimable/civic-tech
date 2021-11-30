"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 30/11/2021
"""


def truncatePrograms(program: str) -> str:
    listProgram = program.split(" ")
    truncProgram = ""
    if len(listProgram) > 40:
        for i in range(40):
            truncProgram += listProgram[i] + " "
        truncProgram += " ..."
    else:
        for i in range(len(listProgram)):
            truncProgram += listProgram[i] + " "
    
    return truncProgram