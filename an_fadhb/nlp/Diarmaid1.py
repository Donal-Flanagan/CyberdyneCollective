
import nltk
import numpy
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter


def create_lexicon(fileIn):
    nltk.download("stopwords")
    nltk.download("punkt")
    stop_words = set(stopwords.words("english"))

    lemmitizer = WordNetLemmatizer()
    lexicon=[]
    tokenizer = RegexpTokenizer(r'\w+')
    with open(fileIn, 'r') as f:
        contents = f.readlines()
        for l in contents[:]:
            all_words = word_tokenize(l)
            for i in all_words:
                if i.lower() not in stop_words:
                    if i.isalnum():
                        lexicon.append(i)

    lexicon = [lemmitizer.lemmatize(i) for i in lexicon]
    print(lexicon)
    w_counts = Counter(lexicon)
    l2 =[]
    for w in w_counts:
        l2.append([w, w_counts[w]])


if __name__ == "__main__":
    print("What I want to print")
    create_lexicon("script1.txt")
