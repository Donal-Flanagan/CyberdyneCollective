Package Info
------------

To use you can install via pip install <package_name>

create_words_and_values
+++++++++++++++++++++++
This takes in a file name, reads in the file, and creates a list of (key-word, value) pairs for each keyword in the file.

evaluate_file
+++++++++++++
This will take in a filename, run create_words_and_values(), and save the result to the filestem.pickle. E.g. if you pass in test.txt, it will save to test.pickle

evaluate_corpus
+++++++++++++++
This takes in the file where a list of words (created from create words and values) is saved, the number of those words you want to check, and the directory holding all the files to check against.
It will then check the top n words against all of the words in the corpus.   It returns a list of (word, value) pairs, as well as a dictionary holding the values for each word for each file in the directory.

get_overall_values_only
+++++++++++++++++++++++
Takes the same inputs as evaluate corpus, but returns only the overall values for the words.

Requirements
------------
To install nltk manually, you can run
<sudo> pip install nltk

The requirements are the nltk datasets: "punkt", "stopwords", and "wordnet". If these fail to download them you can install them manually by opening a python shell and running
import nltk
nltk.download(<datasetname>)
e.g.
nltk.download("punkt")