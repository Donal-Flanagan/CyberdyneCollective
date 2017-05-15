import os
import pickle
from collections import Counter
from operator import itemgetter

from diarmaidi2xpackage import create_words_and_values


def get_all_txt_files_in_directory(directoryIn):
    """
    Get all of the files in the directory which end in .txt

    :param directoryIn: str
        Path to the directory to evaluate
    :return: list 
        list of all files in the directory 
    """

    fileshan=[]
    for root, dirs, files in os.walk(directoryIn):
            for file in files:
                if file.endswith(".txt"):
                    l=os.path.join(root,file)
                    fileshan.append(l)

    return fileshan


def compare_single_file(words_in, file_in):
    """
    Takes as input a list of words and compares it to all words in a file.
    Ranks each word as a percentage of total word count in the file.

    :param words_in: list
        A list of words in string format to be compared to the words in file_in
    :param file_in: str
        The file path for the text to be compared
        
    :return: collections.Counter()
        key: str, word
        value: int, count of occurrences of word in file_in
    """
    results = create_words_and_values(file_in)

    s = sum(results.values())

    overall_value = {}
    for word in words_in:
        k = 100 * results.get(word, 0) / s
        overall_value[word] = k
    return Counter(overall_value)


def compare_file_list(words_in, files_in):
    """
    Compare a list of words with each of the files in, returning a value for each file and an overall value

    :param words_in: list
        A list of words in string format to be compared to all of the files in files_in
    :param files_in: list
        A list of files to be compared
        
    :return: list, dict 
        sorted_values: a list of tuples, with each tuple holding the a word/value pair
        file_values: a dictionary of the values for each file. the dictionary key is the filename (from the file passed in)
    

    """
    overall_value = Counter({})
    file_values = {}

    for file_in in files_in:
        values_out = compare_single_file(words_in, file_in)
        overall_value += values_out
        file_values[file_in] = sorted(values_out.items(), key=itemgetter(1), reverse=True)

    for word in words_in:
        overall_value[word] = overall_value.get(word, 0.0)/len(files_in)

    sorted_values = sorted(overall_value.items(),key=itemgetter(1), reverse=True)
    return sorted_values, file_values


def get_sorted_key_words(file_in):
    """
    Simple subroutine to read in the data
    :param file_in: file to read data from
    :return: a list of sorted words
    """
    x = pickle.load(open(file_in, 'rb'))
    sorted_x = sorted(x.items(), key=itemgetter(1), reverse=True)

    sorted_words = list(map(itemgetter(0), sorted_x))
    return sorted_words

def get_top_values(file_in, n):
    """
    Get the top n values
    :param file_in: file to read values from
    :param n: number of values to get
    :return: a list of size n holding the top n words in the dataset
    """

    sorted_words = get_sorted_key_words(file_in)

    return sorted_words[0:n]


def evaluate_corpus(word_file_in, number_of_words_in, directory_in):

    values = get_top_values(word_file_in, number_of_words_in)

    files = get_all_txt_files_in_directory(directory_in)

    val, file_val = compare_file_list(values, files)
    return val, file_val


def get_overall_values_only(word_file_in, number_of_words_in, directory_in):
    val, file_val = evaluate_corpus(word_file_in, number_of_words_in, directory_in)
    return val


def main():
    file_in = input("Please input the file to load the dataset from")
    number = eval(input("Please input the number of words to use"))

    directory_in = input("Please input the directory holding the corpus of information")
    print(get_overall_values_only(file_in, number, directory_in))

if __name__ == "__main__":
    main()
