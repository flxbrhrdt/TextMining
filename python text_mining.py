import requests
import re, math
from collections import Counter
from operator import itemgetter
import operator

def text_preprocessing(text):
    """Check if the the input is a string or pathfile. convert it to string

    >>> text_preprocessing(4)

    >>> text_preprocessing('4')
    '4'
    """
    if isinstance(text, str):
        if text.endswith('.txt'):
            path = text
            text = open(path,'r')
            return text.read()
        else:
            return text
    else:
        return None

def word_counter(text):
    """return a list with word frequencies

    >>>
    """
    WORD = re.compile(r'\w+')
    text = text_preprocessing(text)
    words = WORD.findall(text)
    wordcount = Counter(words)
    return wordcount

def word_frequency(text):
    """Take a string, count the word frequencies in it and display it in a descending order

    >>> word_frequency('text text hello text python')
    [('text', 3), ('hello', 1), ('python', 1)]
    """
    text = text.lower() #     Preprocessor: all lower case letters
    word_frequency = word_counter(text) #Calling the function
    return sorted(word_frequency.items(), key=lambda pair: pair[1], reverse=True)

def cosine(vec1, vec2):
    """ Calculate the cosine between two vectors, used as a measurment of similarity

    """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    # Check if denominator is any kind of zero, empty container or False
    if denominator is not None:
        return float(numerator) / denominator
    else:
        return 0.0

def Cosine_similarity(text_1, text_2):
    """find similarities between two text files, by looking at the number of word usage

    >>> Cosine_similarity('This is a test.', 'This is the second test.')
    0.6708203932499369
     """
    # WORD = re.compile(r'\w+')
    # transform the two input strings into a vector
    vector_1 = word_counter(text_1)
    vector_2 = word_counter(text_2)
    return cosine(vector_1, vector_2)


def listmaker(*texts):
    """Make a list that gets iterated in the Text_similarity function

    >>> listmaker('a', 'c', 'y', 'x', 'gfhj')
    ['a', 'c', 'y', 'x', 'gfhj']
    """

    text_list=[]
    for a in texts:
        text_list.append(text_preprocessing(a))
    return text_list

def Text_similarity(*texts):
    """compare an indefinite number of texts with each other

    >>> Text_similarity('This is the first test', 'This is the second test, what a Test. One more Test', 'This is the firs test')
    [[0.9999999999999998, 0.49613893835683387, 0.7999999999999998], [0.49613893835683387, 1.0000000000000002, 0.49613893835683387], [0.7999999999999998, 0.49613893835683387, 0.9999999999999998]]
    """
    # print(*texts)
    # Loop through list of Texts
    text = listmaker(*texts)
    sims1 =[]
    for p in range(len(text)):
        sims2 =[]
        for i in range(len(text)):
            sim = Cosine_similarity(text[p], text[i])
            sims2.append(float("{0:.2f}".format(sim)))
        sims1.append(sims2)
    return sims1





text_1 = 'Great Expectations by Dickens.txt'
text_2 = 'A tale of two cities by Dickens.txt'
text_3 = 'Christmas Carol by Dickens.txt'
text_4 = 'Platos Republic by Plato.txt'
text_5 = 'Crito by Plato.txt'
text_6 = 'Metarmophosis by Kafka.txt'
text_7 = 'Moby Dick by Melville.txt'


Text_similarity(text_1, text_2, text_3, text_4, text_5, text_6, text_7)
