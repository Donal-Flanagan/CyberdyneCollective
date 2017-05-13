import nltk
import numpy
from nltk import word_tokenize
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from operator import itemgetter

nltk.download("stopwords")

def get_all_words_in_order(fileIn):
    #We want to lemmatize words so that plurals etc. are counted as the same word
    lemmitizer = WordNetLemmatizer()
    # We are not interested in stop words
    stop_words = set(stopwords.words("english"))
    lexicon=[]
    with open(fileIn, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            for i in all_words:
                if i.lower() not in stop_words:
                    #We don't want numbers or punctuation
                    if i.isalnum():
                        lexicon.append(i.lower())

    lexicon = [lemmitizer.lemmatize(i) for i in lexicon]
    return lexicon

def get_most_important_words(fileIn,n):
    #Get all key words
    key_words = get_all_words_in_order(fileIn)
    key_words = key_words +create_all_key_words(key_words)


    newlist = sort_key_words(key_words)

    return newlist[0:n]

def sort_key_words(listIn):
    w_counts = Counter(listIn)
    l2 = []
    for w in w_counts:
        if (w.count(' ') == 0):
            mult = 1
        else:
            mult = w.count(' ') + 1

        l2.append([w, w_counts[w] * mult])

    l3 = sorted(l2, key=itemgetter(1), reverse=True)

    newlist = [x[:1][0] for x in l3]
    return newlist

#I assumed that key words would follow each other - didn't consider the scenario where key words had words between them
def create_all_key_words(lexiconIn):
    lexicon2 = []
    for i in range(1,len(lexiconIn)-2):
        doubleTest = lexiconIn[i]+" " +lexiconIn[i+1]
        toTest = doubleTest +" " +lexiconIn[i+2]
        for j in range(1,len(lexiconIn)-2):
            testAgainstDouble = lexiconIn[j] +" "+ lexiconIn[j+1]
            testAgainst = testAgainstDouble+" "+ lexiconIn[j+2]
            if (toTest == testAgainst):
                lexicon2.append(toTest)
            if (testAgainstDouble == doubleTest):
                lexicon2.append(doubleTest)

    return lexicon2





if __name__ == "__main__":
    list = get_most_important_words("script.txt",5)
    print (list)