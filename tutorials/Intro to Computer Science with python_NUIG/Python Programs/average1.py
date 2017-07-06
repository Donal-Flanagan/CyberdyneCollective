#  average1.py

def main():
    n = input("How many numbers do you have? ")
    sum = 0.0
    for i in range(n):
        x = input("Enter a number >> ")
        sum = sum + x
    print "\nThe average of the numbers is %f.\n" % (sum/n)

main()
