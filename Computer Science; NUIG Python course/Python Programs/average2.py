# average2.py: interactive loop

def main():
    sum = 0.0
    count = 0
    more = "yes"
    while more[0] == "y":
        x = input("Enter a number >> ")
        sum = sum + x
        count = count + 1
        more = raw_input("Do you have more numbers (yes or no)? ")
    print "\nThe average of the numbers is %f.\n" % (sum/count)

main()
