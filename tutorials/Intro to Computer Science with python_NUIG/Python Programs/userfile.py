# userfile.py
#  Program to create a file of user names in batch mode.

import string

def main():
    print "This program creates a file of usernames from a"
    print "file of names."

    # get the file names
    inName = raw_input("What files are the names in?")
    outName = raw_input("What files should the usernames go in?")

    # open the files
    inFile = open(inName, 'r')
    outFile = open(outName, 'w')

    # process each line of the input file
    for line in inFile:

        # get first and last names
        first, last = string.split(line)

        # create the username
        uname = string.lower(first[0] + last[:7])

        print  first, last, "-->", uname

        # write it to the output file
        outFile.write(uname + '\n')

    # close the files
    inFile.close()
    outFile.close()

    print "Usernames have been written to", outName

main()
