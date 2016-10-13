# whatsn.py
# a program to do things to n
#
# by Dónal
def sumN(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range (1,n+1):
        sum = sum + (i**3)
    return sum


def main():
    n = input("Please enter a value for n:")

    x = sumN(n)

    y = sumNCubes(n)

    print "The sum of the first ",n," positive integers is ",x
    print "and the sum of the cubes of the first",n," positive integers is",y

main()
