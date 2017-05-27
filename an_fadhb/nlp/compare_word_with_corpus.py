from create_word_value import create_words_and_values
import pickle
from operator import itemgetter
import os
from collections import Counter

def compare_directory(words_in, directoryIn):
    fileshan=[]
    for root, dirs, files in os.walk(directoryIn):
            for file in files:
                if file.endswith(".txt"):
                    l=os.path.join(root,file)
                    fileshan.append(l)

    sorted_values=compare_file_list(words_in, fileshan)

    return sorted_values


def compare_single_file(words_in, file_in):
    results = create_words_and_values(file_in)

    s = sum(results.values())

    overall_value = {}
    for word in words_in:
        k = 100 * results.get(word, 0) / s
        overall_value[word] = overall_value.get(word, 0.0) + k
    return Counter(overall_value)


def compare_file_list(words_in, files_in):
    overall_value = Counter({})

    for file_used in files_in:
            overall_value=overall_value+compare_single_file(words_in,file_used)

    for word in words_in:
        overall_value[word] = overall_value.get(word, 0.0)/len(files_in)

    sorted_values = sorted(overall_value.items(),key=itemgetter(1), reverse=True)
    return sorted_values


def get_sorted_key_words(file_in):
    x = pickle.load(open(file_in, 'rb'))
    sorted_x = sorted(x.items(), key=itemgetter(1), reverse=True)

    sorted_words = list(map(itemgetter(0), sorted_x))
    return sorted_words

def get_top_values(file_in, n):

    sorted_words = get_sorted_key_words(file_in)

    return sorted_words[0:n]


def main():

   # file_in = input("Please input the file to load the dataset from")
    file_in='test.pickle'
   # number = eval(input("Please input the number of words to use"))
    number = 20

    values = get_top_values(file_in, number)

    files = ['transcript_1.txt', 'transcript_2.txt', 'transcript_3.txt']

    val = compare_file_list(values, files)

    print(val)

    val2 =compare_directory(values, ".")
    print(val2)

if __name__ == "__main__":
    main()
