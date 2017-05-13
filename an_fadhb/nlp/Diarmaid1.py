
import nltk
import numpy
from nltk import word_tokenize
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from operator import itemgetter

nltk.download("pefunkt")
nltk.download("stopwords")
nltk.download("wordnet")

def get_lemitized_words_in_order(fileIn):
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

#Return the top n words in the database.   fileIn is the path to the file, and n is the number of words to get
def get_most_important_words(fileIn,n):
    #Get all key words

    key_words = create_all_key_words(fileIn)

    newlist = sort_key_words(key_words)

    return newlist.head(n)


'''This is where you rank the words. Takes in a list of words, and returns a list of lists, with the inner list holding the word and the value
[
 [word, value],
 [word, value],
 [word, value],
    :       :
    :       :
 [word, value],
 [word, value],
 [word, value]
]
'''
def assignValue(words):
    w_counts = Counter(words)
    word_and_value = []
    for w in w_counts:
        if (w.count(' ') == 0):
            mult = 1
        else:
            mult = w.count(' ') + 1

        word_and_value.append([w, w_counts[w] * mult])
    return word_and_value

'''Sort the keyValue so that the best resuls are at the top.   Assumes input is a list of lists, with the inner list holding the word and the value
[
 [word, value],
 [word, value],
 [word, value],
    :       :
    :       :
 [word, value],
 [word, value],
 [word, value]
]
'''
def sort_key_words(listIn):
    listIn.sort(key=itemgetter(1), reverse=True)
    newlist = [x[:1][0] for x in listIn]
    return newlist

'''This is where I create all of the key words.   I assume that keywords will appear in the text in order,
and the maximum length of the key words is 3. Stop words can appear between keywords.

'''
def create_all_key_words(fileIn):
    lexicon2 = []

    key_words = get_lemitized_words_in_order(fileIn)

    for i in range(1, len(key_words)-2):
        doubleTest = key_words[i] + " " + key_words[i + 1]
        toTest = doubleTest +" " + key_words[i + 2]
        for j in range(1, len(key_words)-2):
            testAgainstDouble = key_words[j] + " " + key_words[j + 1]
            testAgainst = testAgainstDouble+" " + key_words[j + 2]
            if (toTest == testAgainst):
                lexicon2.append(toTest)
            if (testAgainstDouble == doubleTest):
                lexicon2.append(doubleTest)

    return lexicon2



def main():
    number = eval(input("How many words do you want to get?"))

    list = get_most_important_words("script.txt", number)
    print (list)

if __name__ == "__main__":
    main()