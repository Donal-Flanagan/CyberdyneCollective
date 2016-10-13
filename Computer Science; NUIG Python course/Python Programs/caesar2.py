#  text2numbers.py
#  A program to convert a text message into a sequence of numbers
#  according to the underlying ASCII encoding.

def main():
    print "This program converts a text message into a sequence"
    print "of numbers representing the ASCII encoding of the message."
    print

    # get the message
    message = raw_input("Please enter the message to encode: ")

    print
    print "These are the ASCII codes:"

    # loop over the message a print out the ASCII values.
    for c in message:
        a=ord(c)
        a+5=b
        print 

    print

main()
