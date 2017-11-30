# pi.py
# a program to deduce pi, to increasing degrees
# of accuracy, from a mathematical series
#
# by Dónal

def main():
    n = input("Please enter the number of terms to sum: ")
    y = 0

    for i in range(1,n*2,2):
        z = -((-1)**((i+1)/2))
        y = y + ((4/i)*z)

    print "Pi is equal to", y

main()
