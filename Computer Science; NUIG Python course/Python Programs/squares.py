# squares.py
# a program to find the sum of the first n
# natural numbers where n is defined by the user
#
#by Dónal

def main():
    n = input("Please enter a value for n:")
    y = 0

    for i in range(n):
        y = y + ((i+1)**3)

    print "The sum of the cubes of the first", n,"natural numbers is", y

main()

    
