# average7.py: nested loop

import string

def main():
    name = raw_input("What file are the numbers in? ")
    file = open(name, 'r')
    sum = 0.0
    count = 0
    line = file.readline()
    while line != "":
        for x in string.split(line):
            sum = sum + eval(x)
            count = count + 1
        x = file.readline()
    print "\nThe average of the numbers is %f.\n" % (sum/n)

main()
