# average.py
# a program to calculate the average of a series of numbers
#
# by Dónal

def main():
    n = input("Please enter the amount of numbers to be entered: ")
    x = 0

    for i in range(n):
        y = input("Please enter the number to be calculated: ")
        x = x + y


    z = x/n
    print "The average of the numbers is", z

main()

