
import nltk
import numpy
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter


def create_lexicon(fileIn):

    stop_words = set(stopwords.words("english"))

    lemmitizer = WordNetLemmatizer()
    lexicon=[]
    with open(fileIn, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            lexicon += list(all_words)
    lexicon2 = [lemmitizer.lemmatize(i) for i in lexicon if i ]
    w = Counter(lexicon2)
    for w2 in w:
        l=1
  #      print(w[w2])
 #   print(lexicon2)






if __name__ == "__main__":
    print("What I want to print")
    nltk.download("stopwords")
    create_lexicon("script1.txt")