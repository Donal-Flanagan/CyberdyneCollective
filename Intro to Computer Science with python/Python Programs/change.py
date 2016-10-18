# change.py
#    A program to calculate the value of some change

def main():
    print "Change Counter"
    print
    print "Please enter the number of coins of each type."
    cent1 = input("Number of 1 cent coins: ")
    cent2 = input("Number of 2 cent coins: ")
    cent5 = input("Number of 5 cent coins: ")
    cent10 = input("Number of 10 cent coins: ")
    cent20 = input("Number of 20 cent coins: ")
    cent50 = input("Number of 50 cent coins: ")
    total = .01 * cent1 + .02 * cent2 + .05 * cent5
    total = total + .1 * cent10 + .2 * cent20 + .5 * cent50
    print
    print "The total value of your change is", total

main()
