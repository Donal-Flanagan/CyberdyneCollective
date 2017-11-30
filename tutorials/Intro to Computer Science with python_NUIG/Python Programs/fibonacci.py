# fibonacci.py
# a program to compute the nth fibonacci number.
#
# by Dónal

def main():
    n = input("Please input n: ")
    f = 1

    for i in range(n-1):
        f = f + i

    print "The",n,"th number in the Fibonacci sequence is", f

main()
