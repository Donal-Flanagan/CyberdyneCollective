# convert5.py
#
# a program to convert pints of beer into litres of beer
# by Dónal

def main():
    print "This program converts pints of beer into the equivalent measurement in litres of beer."
    pints = input("How many pints of beer do you have?")
    litres = pints * 0.57
    print "You have", litres, "litres of beer."

main()
