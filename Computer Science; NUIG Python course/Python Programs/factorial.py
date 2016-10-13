# factorial.py
#
#  A program to compute the factorial of a number,
#  illustrates the accumulator pattern.

def main():
    n = input("Enter a positive integer, please: ")
    product = 1
    for factor in range(2, n+1):
        product = product * factor

    print "The factorial of", n, "is", product

main()
    
