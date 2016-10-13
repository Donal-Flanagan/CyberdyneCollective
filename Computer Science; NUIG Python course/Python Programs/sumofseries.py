# sumofseries.py
# a program to calculate the sum of a series of numbers entered by the user
#
# by Dónal

def main():
    x = input("How many numbers are to be summed?")
    y = 0

    for i in range(x):
        n = input("Enter number to be summed: ")
        y = y + n

    print "The sum of these numbers is", y

main()
