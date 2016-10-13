# a program to calculate fibonacci numbers.

def main():
    print "this program calculates the n-th number"
    print "in the fibonacci sequence 1, 1, 2, 3, 5, 8, ..."
    
    n = input("Enter n: ")

    old, new = 0, 1
    print old,
    for i in range(n):
        old, new = new, old + new
        print old,

    print
    print "the n-th Fibonacci number is ", old

main()
    
