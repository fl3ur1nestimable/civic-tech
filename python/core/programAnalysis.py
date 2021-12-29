"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 30/11/2021
"""

# Import needed packages
from typing import List, Tuple
from string import punctuation
import unidecode


# Import personal modules
from python.core.coreJson import read_json
from python.core.coreTxt import open_txt



def countWordFrequency(program: str) -> Tuple[dict, List[str]]:
    """
        Function to count the frequency of words in a given text

        Parameters :
            - program (string) : A given program text
        
        Returns :
            - dataWords (dict) : the sorted frequency of words in the text
            - wordsList (list) : the list of all words in the program
    """
    # Change program's word to lowered words
    program = program.lower()
    program = unidecode.unidecode(program)



    # Remove accent and punctuation from the program
    for item in punctuation+"\n":
        program = program.replace(item, " ")

    # Change program's word to remove potential empty words
    wordsList = program.split(" ")
    wordsList = removeAllOccurence(wordsList, [''])
    
    dataWords = {}

    for words in wordsList:
        if words not in dataWords:
            cpt = wordsList.count(words)
            dataWords[words] = cpt

    return dataWords, wordsList


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


def rateDataWords(program: str) -> List[float]:
    """
        Function to count the frequency of words in a given text

        Parameters :
            - program (string) : A given program text
        
        Returns :
            - topicGrades (List[float]) : the rates for each topics of the program
    """
    
    dataWords, _ = countWordFrequency(program)

    keyWords = read_json('keyWords')

    topics = ["environments", "social", "economic"]
    topicGrades = [0, 0, 0]
    topicIndex = 0

    for topic in topics:
        tempGrade = 0

        for word in keyWords[topic]:
            if word in dataWords:
                tempGrade += keyWords[topic][word] * dataWords[word]
        
        topicGrades[topicIndex] = tempGrade
        
        topicIndex += 1
    
    totalGrade = topicGrades[0] + topicGrades[1] + topicGrades[2]
    if totalGrade != 0:
        topicGrades[0], topicGrades[1], topicGrades[2] = round((topicGrades[0] / totalGrade) * 100, 2), round((topicGrades[1] / totalGrade) * 100, 2), round((topicGrades[2] / totalGrade) * 100, 2)

    return topicGrades


def lastOccurencyIndex(reversedList: List[str], word: str) -> int:
    """
        Function to return the index of the last occurency of a word in a list

        Parameters :
            - reversedList (List[string]) : reversed list you want to get the index from
            - word (string) : word you want to search in the list
        
        Returns :
            - _ (integer) : the needed index
    """

    listLen = len(reversedList)
    return (listLen - reversedList.index(word) - 1)


# Starts the script with : python3 -m py.core.programAnalysis / python3 -i -m py.core.programAnalysis
if __name__ == "__main__":
    fileData = open_txt('exempleProgram')
    dataWords, wordsList = countWordFrequency(fileData)

    # print(dataWords)
    topicGrades = rateDataWords(dataWords, wordsList)
    print(topicGrades)