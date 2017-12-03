# average6.py: file loop

def main():
    name = raw_input("What file are the numbers in? ")
    file = open(name, 'r')
    sum = 0.0
    count = 0
    x = file.readline()
    while x != "":
        sum = sum + eval(x)
        count = count + 1
        x = file.readline()
        
    print "\nThe average of the numbers is %f.\n" % (sum/count)

main()
