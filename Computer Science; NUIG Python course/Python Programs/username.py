# simple string processing: generate user name

def main ():
    print "This program generates computer user names."
    print

    # get first and last name
    first = raw_input("first name (all lowercase): ")
    last = raw_input("last name  (all lowercase) ")

    # build username
    uname = first[0] + last[:7]

    # output the new name
    print "Your username is ", uname


main()
