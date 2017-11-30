# wordaverage.py
# a program to calculate the average length of the words in a sentence
#
# by Dónal

def main():
    sentence = raw_input("Please enter a sentence:")
    x = string.split(sentence)
    y = len(x)
    letters = 0.0

    for word in x:
        letters = letters + len(word)

    average = letters/y
    print average

main()

    
