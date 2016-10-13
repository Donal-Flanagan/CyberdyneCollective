# numbers2text.py
#  A program to convert a sequence of ASCII codes into a string of text

import string  #  the string library

def main():
    print "This program converts a sequence of ASCII codes"
    print "into the string of text that it represents."
    print

    #  get the encoded message
    print "Please enter the ASCII-encoded message:"
    code = raw_input()

    # loop through the code and build message.
    message = ""
    for num in string.split(code):
        n = eval(num)
        message = message + chr(n)

    print "The decoded message is:", message

main()
