# counter.py
# a program to count the number of words in a sentence
#
# by D�nal

def main():
    import string
    sentence = raw_input("Please enter your sentence:")
    amount = string.split(sentence)
    y = len(amount)
    print "There are ",y,"words in this sentence."
main()
