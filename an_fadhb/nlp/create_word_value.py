
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





def assign_value(words):
    """
    This is where you rank the words. 
    """
    d={}
    w_counts = Counter(words)
    for w in w_counts:
        if w.count(' ') == 0:
            mult = 1.0
        else:
            mult = w.count(' ') + 1.0

        d[w]=w_counts[w]*mult

    return d


def get_lemitized_words_in_order(file_in):
    # We want to lemmatize words so that plurals etc. are counted as the same word
    lemmitizer = WordNetLemmatizer()
    # We are not interested in stop words
    stop_words = set(stopwords.words("english"))
    lexicon=[]
    with open(file_in, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            for i in all_words:
                if i.lower() not in stop_words:
                    # We don't want numbers or punctuation
                    if i.isalnum():
                        lexicon.append(i.lower())

    lexicon = [lemmitizer.lemmatize(i) for i in lexicon]
    return lexicon


def create_all_key_words(file_in):
    """
    This is where I create all of the key words.   I assume that keywords will appear in the text in order,
    and the maximum length of the key words is 3. Stop words can appear between keywords.
    :param file_in:
    :return:
    """
    lexicon2 = []

    key_words = get_lemitized_words_in_order(file_in)

    for i in range(1, len(key_words)-2):
        double_keyword = key_words[i] + " " + key_words[i + 1]
        triple_keyword = double_keyword + " " + key_words[i + 2]
        key_words.append(double_keyword)
        key_words.append(triple_keyword)

    return key_words


def create_words_and_values(file_in):
    """
    Return the top n words in the database.
    file_in is the path to the file, and n is the number of words to get
    """
    # Get all key words
    key_words = create_all_key_words(file_in)

    words_and_values = assign_value(key_words)

    return words_and_values


def main():
    # number = eval(input("How many words do you want to get?"))

    #file_in = input("Please input the file to create the list from")
    file_in = "script1.txt"
    #save_file = input("Please input the save file name")
    save_file = "test.pickle"
    print("Calculating values from" , file_in, " and saving list to ", save_file)

    results = create_words_and_values(file_in)
    print(results)
    print(save_file)

    pickle.dump(results, open(save_file, 'wb'))

    test = pickle.load(open(save_file,'rb'))

    print(test)

if __name__ == "__main__":
    main()
