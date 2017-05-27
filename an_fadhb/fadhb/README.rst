Package Info
------------

To install diarmaidi2xpackage, clone this repository, and go into the folder and run 'pip install .'. This will install
diarmaidi2xpacakge together with the requirements to your system.

To Use
------

import diarmaidi2xpackage gives you the following commands:

create_words_and_values
+++++++++++++++++++++++
This takes in a file name, reads in the file, and creates a list of (key-word, value) pairs for each keyword
in the file.

input: filename

output: dict[word]=value

evaluate_file
+++++++++++++
This will take in a filename, run create_words_and_values(), and save the result to the filestem.pickle. E.g. if you
pass in test.txt, it will save to test.pickle.

Run this to create the list of file/value pairs for a given file.

get_top_values
++++++++++++++
Select from a previously generated word/value list (stored in a file) the top n entries in the list.

input: file_name, number_of_entries

output: [words] <-size n

compare_single_file
+++++++++++++++++++
Takes as input a list of words and compares it to all words in a file. Ranks each word as a percentage of total word
values in the file.

input: [words_in], file

output: [(word, value),(word, value),(word, value)]

compare_file_list
+++++++++++++++++
Takes as input a list of words to compare and a list of files to compare it to. Returns the average of the percentage
value over all files, together with the percentage values for each word for each file

input: [words_in], file_list

output: [(word, value),(word, value),(word, value)], dict[file_in_file_list]=[(word, value),(word, value),(word, value)]

evaluate_corpus
+++++++++++++++
This takes in the file where a list of words (created from create words and values) is saved, the number of those words
you want to check, and the directory holding all the corpus of files to check against.  It will scan the directory to
get all files which end in .txt, and consider that list of files as the corpus.   It gets the value of the input list
in comparison to each individual file, and overall.

input: fileName(holding dict of word/value pairs), number, directory

output: [(word, value),(word, value),(word, value)], dict[fileInDirectory]=[(word, value),(word, value),(word, value)]

get_overall_values_only
+++++++++++++++++++++++
Takes the same inputs as evaluate corpus, but returns only the overall values for the words.

Requirements
------------
To install nltk manually, you can run
<sudo> pip install nltk

The requirements are the nltk datasets: "punkt", "stopwords", and "wordnet". If these fail to download them you can
install them manually by opening a python shell and running

>>>import nltk

>>>nltk.download(<dataset>)

>>>nltk.download("punkt")
