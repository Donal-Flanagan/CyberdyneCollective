# sum.py
# a program to calculate the sum of the first n natural numbers
# where n is provided by the user
#
# by Dónal

def main():
    n = input("Please input a value for n:")
    no = n
    sum = 0
    for i in range(n):
        sum = sum + (i+1)

    print "The sum of the first", no ,"natural numbers is", sum

main()
