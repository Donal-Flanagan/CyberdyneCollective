from Diarmaid1 import create_words_and_values
import pickle
from operator import itemgetter

def compare_words(words_in, files_in):
    overall_value = {}

    print(words_in)
    for file in files_in:
        results = create_words_and_values(file)

        s = sum(results.values())
        print(s)
        for word in words_in:
            k = 100*results.get(word,0)/s
            overall_value[word]=overall_value.get(word,0.0)+k
            #overall_value[word]= overall_value.get(word, default=0)+results.get(word, default=0)
    for word in words_in:
        overall_value[word] = overall_value.get(word, 0)/len(files_in)


    print(overall_value)

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
    number = 40

    values = get_top_values(file_in, number)

    print(values)
    files = ['transcript_1.txt', 'transcript_2.txt', 'transcript_3.txt']

    val = compare_words(values, files)

    print(val)


if __name__ == "__main__":
    main()