"""
    Author : Cheneviere Thibault & Hashani Elion
    Mail : thibault.cheneviere@telecomnancy.eu & elion.hashani@telecomnancy.eu
    Date : 29/12/2021 & 02/01/2022
"""

# Import needed modules
import pathlib, sys, pytest
from _pytest.monkeypatch import V

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

    test3 = ""
    dict3 = {}
    list3 = []
    result3 = (dict3,list3)

    assert type(countWordFrequency(test1)) is tuple

    assert countWordFrequency(test1) == result1
    assert countWordFrequency(test2) == result2
    assert countWordFrequency(test3) == result3

    with pytest.raises(AssertionError): ## AssertionError ##
        test4 = "Lorem ipsum 987"
        dict4 = {"lorem" : 1, "ipsum" : 1, "987" : 1 }
        list4 = ["lorem", "ipsum", "987", "erreur"]
        result4 = (dict4,list4)
        assert countWordFrequency(test4) == result4





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

    test3 = []
    pattern3 = ["oui"]
    result3 = []

    assert removeAllOccurence(test3,pattern3) == result3

    test4 = ["oui"]
    pattern4 = []
    result4 = ["oui"]

    assert removeAllOccurence(test4,pattern4) == result4

    with pytest.raises(AssertionError):
        test5 = ["oui", "oui", "non"]
        pattern5 = "oui","non"
        result5 = ["oui"]

        assert removeAllOccurence(test5,pattern5) == result5





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

    with pytest.raises(ValueError): ## ValueError: 'elion' is not in list ##
        test3 = ["test", "jean", "te", "ben", "louis", "thib", "", "1", "jean", ""]
        word3 = "elion"
        lastOccurencyIndex(test3, word3)

    with pytest.raises(ValueError): ## ValueError: 1 is not in list ##
        test4 = ["test", "jean", "te", "ben", "louis", "thib", "", "1", "jean", ""]
        word4 = 1 ## int instead of str ##
        lastOccurencyIndex(test4, word4)


def test_rateDataWords():
    test1 = "Lorem ipsum dolor sit amet."
    result1 = [0, 0, 0]

    test2 = "Une entreprise commerciale et sociale."
    result2 = [0, round(4/14*100, 2), round(10/14*100, 2)]

    assert type(rateDataWords(test1)) is list

    assert rateDataWords(test1) == result1
    assert rateDataWords(test2) == result2

    with pytest.raises(AttributeError): ## AttributeError: 'int' object has no attribute 'lower' ##
        test3 = 98
        rateDataWords(test3)