# average4.py: sentinel loop

def main():
    sum = 0.0
    count = 0
    x = raw_input("Enter a number (<Enter> to quit) >> ")
    while x != "":
        sum = sum + eval(x)
        count = count + 1
        x = raw_input("Enter a number (<Enter> to quit) >> ")
    print "\nThe average of the numbers is %f.\n" % (sum/count)

main()
