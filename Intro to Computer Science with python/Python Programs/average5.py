# average5.py: file loop

def main():
    name = raw_input("What file are the numbers in? ")
    file = open(name, 'r')
    sum = 0.0
    count = 0
    for x in file:
        sum = sum + eval(x)
        count = count + 1
    print "\nThe average of the numbers is %f.\n" % (sum/n)

main()
