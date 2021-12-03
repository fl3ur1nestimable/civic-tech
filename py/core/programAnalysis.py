"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 30/11/2021
"""

# Import needed packages
from typing import List, Tuple
from string import punctuation
from unidecode import unidecode


# Import personal modules
from py.core.coreJson import read_json
from py.core.coreTxt import open_txt



def countWordFrequency(program: str) -> Tuple[dict, int]:
    """
        Function to count the frequency of words in a given text

        Parameters :
            - program (string) : A given program text
        
        Returns :
            - dataWords (dict) : the sorted frequency of words in the text
    """
    # Change program's word to lowered words
    program = program.lower()



    # Remove accent and punctuation from the program
    for item in punctuation+"\n":
        program = program.replace(item, " ")

    # Change program's word to remove potential empty words
    wordsList = program.split(" ")
    wordsList = removeAllOccurence(wordsList, [''])

    nbWords = len(wordsList)
    
    dataWords = {}

    for words in wordsList:
        if words not in dataWords:
            cpt = wordsList.count(words)
            words = unidecode(words)
            dataWords[words] = cpt

    return dataWords, nbWords


def removeAllOccurence(argList: List, pattern: List[str]) -> str:
    """
        Function to remove all occurences of string in a pattern list from a given list

        Parameters :
            - argList (List) : list you want to formate
            - pattern (List[string]) : caracters you want to delete from the words list
        
        Returns :
            - returnList (List) : the formated list
    """
    
    returnList = []
    for item in argList:
        if not item in pattern:
            returnList.append(item)
    return returnList


def rateDataWords(dataWords: dict, nbWords: int) -> float:
    keyWords = read_json('keyWords')

    topics = ["environments", "social", "economic"]
    globalGrade = 0

    for topic in topics:
        tempGrade = 0

        for word in keyWords[topic]:
            if word in dataWords:
                tempGrade += (keyWords[topic][word] / 5) * dataWords[word]
        
        globalGrade += tempGrade / nbWords
    
    return globalGrade



# Starts the script with : python3 -m py.core.programAnalysis
if __name__ == "__main__":
    text = '''Auxerunt haec vulgi sordidioris audaciam, quod cum ingravesceret penuria 
    commeatuum, famis et furoris inpulsu Eubuli cuiusdam inter suos clari domum ambitiosam ignibus subditis 
    inflammavit rectoremque ut sibi iudicio imperiali addictum calcibus incessens et pugnis conculcans seminecem 
    laniatu miserando discerpsit. post cuius lacrimosum interitum in unius exitio quisque imaginem periculi 
    sui considerans documento recenti similia formidabat.

    Ultima Syriarum est Palaestina per intervalla magna protenta, cultis abundans terris et nitidis et civitates 
    habens quasdam egregias, nullam nulli cedentem sed sibi vicissim velut ad perpendiculum aemulas: Caesaream, 
    quam ad honorem Octaviani principis exaedificavit Herodes, et Eleutheropolim et Neapolim itidemque Ascalonem 
    Gazam aevo superiore exstructas.

    Accedebant enim eius asperitati, ubi inminuta vel laesa amplitudo imperii dicebatur, et iracundae 
    suspicionum quantitati proximorum cruentae blanditiae exaggerantium incidentia et dolere inpendio simulantium, 
    si principis periclitetur vita, a cuius salute velut filo pendere statum orbis terrarum fictis vocibus exclamabant.'''

    fileData = open_txt('exempleProgram')
    dataWords, nbWords = countWordFrequency(fileData)

    print(dataWords, nbWords)
    print(rateDataWords(dataWords, nbWords))