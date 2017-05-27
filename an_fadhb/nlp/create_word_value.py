
import nltk
import numpy
import pickle
from nltk import word_tokenize
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from operator import itemgetter


nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")





def get_keywords_and_values(words):
    """
    This is where you rank the words. 
    """
    d={}
    triple_keyword_value = 5
    double_keyword_value= 3
    single_keyword_occurance_value = 1

    stop_words = set(stopwords.words("english"))

    for i in range(0, len(words)-2):
        if words[i] not in stop_words and words[i].isalnum():
            d[words[i]] = d.get(words[i],0.0)+ single_keyword_occurance_value
            if words[i+1] not in stop_words and words[i+1].isalnum():
                d[words[i]+" "+words[i+1]] = d.get(words[i]+" "+words[i+1],0.0)+double_keyword_value
                if words[i + 2] not in stop_words and words[i + 2].isalnum():
                    d[words[i]+" "+words[i+1]+" "+words[i+2]] = d.get(words[i]+" "+words[i+1]+" "+words[i+2],0.0)+triple_keyword_value

    print(i, len(words))

    if words[i+1] not in stop_words and words[i+1].isalnum():
        d[words[i+1]] = d.get(words[i+1],0.0)+ single_keyword_occurance_value
        if words[i+2] not in stop_words and words[i+2].isalnum():
             d[words[i+1]+" "+words[i+2]] = d.get(words[i+1]+" "+words[i+2],0.0)+double_keyword_value
    if words[i+2] not in stop_words and words[+2].isalnum():
        d[words[i+2]] = d.get(words[i+2],0.0)+ single_keyword_occurance_value
    return d


def get_lemitized_words_in_order(file_in):
    # We want to lemmatize words so that plurals etc. are counted as the same word
    lemmitizer = WordNetLemmatizer()
    # We are not interested in stop words

    lexicon=[]
    with open(file_in, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            for i in all_words:
                lexicon.append(i.lower())
    lexicon = [lemmitizer.lemmatize(i) for i in lexicon]
    return lexicon




def create_words_and_values(file_in):
    """
    Return the top n words in the database.
    file_in is the path to the file, and n is the number of words to get
    """
    # Get all key words
    words_in_order = get_lemitized_words_in_order(file_in)

    words_and_values = get_keywords_and_values(words_in_order)

    return words_and_values

def save_words_and_values(file_in, save_file):

    results = create_words_and_values(file_in)

    pickle.dump(results, open(save_file, 'wb'))

def main():
    # number = eval(input("How many words do you want to get?"))

    #file_in = input("Please input the file to create the list from")
    file_in = "script1.txt"
    #save_file = input("Please input the save file name")
    save_file = "test.pickle"
    print("Calculating values from" , file_in, " and saving list to ", save_file)

    save_words_and_values(file_in,save_file)

if __name__ == "__main__":
    main()
