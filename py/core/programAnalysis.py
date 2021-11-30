"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 30/11/2021
"""

# Import needed packages
from typing import List, Tuple
import re



def countWordFrequency(program: str) -> List[Tuple[int, str]]:
    """
        Function to count the frequency of words in a given text

        Parameters :
            - program (string) : A given program text
        
        Returns :
            - dataWords (List[Tuple[integer, string]) : the sorted frequency of words in the text
    """
    
    wordsList = program.split(" ")
    wordsList = formatinWordsList(wordsList, [' ', '\n', ''])
    
    dataWords = []
    passedWords = []
    for words in wordsList:
        if words not in passedWords:
            cpt = wordsList.count(words)
            dataWords.append((cpt, words))
            passedWords.append(words)

    dataWords.sort(reverse=True)

    return dataWords


def formatinWordsList(wordsList: List[str], pattern: List[str]) -> List[str]:
    """
        Function to formate the words in a list and remove words in the pattern List

        Parameters :
            - wordsList (List[string]) : the given words list to formate
            - pattern (List[string]) : words you want to delete from the words list
        
        Returns :
            - returnList (List[string]) : the formated words list
    """

    returnList = []

    for i in range(len(wordsList)):
        if wordsList[i] not in pattern and re.search("[, \. \n :]+", wordsList[i]) is None:
            returnList.append((wordsList[i]).lower())
        elif wordsList[i] not in pattern and re.search("[, \. \n :]+", wordsList[i]) is not None:
            returnList.append(removeAllOccurence(wordsList[i], [".", ":", ",", "\n"]).lower())
    
    return returnList


def removeAllOccurence(word: str, pattern: List[str]) -> str:
    """
        Function to remove all occurences of caracters in a pattern list from a given word

        Parameters :
            - word (string) : word you want to formate
            - pattern (List[string]) : caracters you want to delete from the words list
        
        Returns :
            - returnStr (string) : the formated word
    """
    
    returnStr = ""
    for letters in word:
        if not letters in pattern:
            returnStr += letters
    return returnStr


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

    dataWords = countWordFrequency(text)

    print(dataWords)