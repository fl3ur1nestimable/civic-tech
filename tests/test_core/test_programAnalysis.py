"""
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 29/12/2021
"""

# Import needed modules
import pathlib, sys

# Add parent dir to the path
cwd = pathlib.Path(__file__).parents[2]
parentdir = str(cwd)
sys.path.append(parentdir)


# Import personal modules
from python.core.programAnalysis import countWordFrequency, lastOccurencyIndex, rateDataWords, removeAllOccurence



def test_countWordFrequency():
    test1 = "Lorem ipsum dolor sit amet."

    dict1 = {
        "lorem": 1,
        "ipsum": 1,
        "dolor": 1,
        "sit": 1,
        "amet": 1
    }
    list1 = ["lorem", "ipsum", "dolor", "sit", "amet"]
    result1 = (dict1, list1)

    test2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ullamcorper facilisis orci, ac dictum felis imperdiet at. Quisque eget est. Quisque eget est."

    dict2 = {
        "lorem": 1,
        "ipsum": 1,
        "dolor": 1,
        "sit": 1,
        "amet": 1,
        "consectetur": 1,
        "adipiscing": 1,
        "elit": 1,
        "nulla": 1,
        "ullamcorper": 1,
        "facilisis": 1,
        "orci": 1,
        "ac": 1,
        "dictum": 1,
        "felis": 1,
        "imperdiet": 1,
        "at": 1,
        "quisque": 2,
        "eget": 2,
        "est": 2
    }
    list2 = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "nulla", "ullamcorper", "facilisis", "orci", "ac", "dictum", "felis", "imperdiet", "at", "quisque", "eget", "est", "quisque", "eget", "est"]
    result2 = (dict2, list2)

    assert type(countWordFrequency(test1)) is tuple

    assert countWordFrequency(test1) == result1
    assert countWordFrequency(test2) == result2


def test_removeAllOccurence():
    test1 = ["test", "te", "ben", "louis", "thib", "", "1", "jean", ""]
    pattern1 = [""]
    result1 = ["test", "te", "ben", "louis", "thib", "1", "jean"]

    test2 = ["test", "te", "ben", "louis", "thib", "", "1", "jean", "", "ben", "jean", "", "thib"]
    pattern2 = ["", "jean"]
    result2 = ["test", "te", "ben", "louis", "thib", "1", "ben", "thib"]

    assert type(removeAllOccurence(test1, pattern1)) is list

    assert removeAllOccurence(test1, pattern1) == result1
    assert removeAllOccurence(test2, pattern2) == result2


def test_lastOccurencyIndex():
    test1 = ["test", "jean", "te", "ben", "louis", "thib", "", "1", "jean", ""]
    word1 = "jean"
    result1 = 8

    test2 = ["test", "jean", "te", "ben", "louis", "thib", "", "1", "jean", "", "ben"]
    word2 = "ben"
    result2 = 7

    assert type(lastOccurencyIndex(test1, word1)) is int

    assert lastOccurencyIndex(test1, word1) == result1
    assert lastOccurencyIndex(test2, word2) == result2


def test_rateDataWords():
    test1 = "Lorem ipsum dolor sit amet."
    result1 = [0, 0, 0]

    test2 = "Une entreprise commerciale et sociale."
    result2 = [0, round(4/14*100, 2), round(10/14*100, 2)]

    assert type(rateDataWords(test1)) is list

    assert rateDataWords(test1) == result1
    assert rateDataWords(test2) == result2