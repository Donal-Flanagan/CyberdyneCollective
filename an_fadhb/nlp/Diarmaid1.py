#There was no definition of what important means, so I am assuming that important means repeated.
#

import nltk
import numpy
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

def create_lexicon(fileIn):
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
        print(w[w2])
    print(lexicon2)
