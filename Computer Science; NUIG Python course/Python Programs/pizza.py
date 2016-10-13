# pizza.py
# a program to calculate the cost per square inch of a circular pizza
#
# by Dónal

def main():
    x = input("Please enter the price of the pizza:")
    d = input("Please enter the diameter of the pizza in inches:")
    r = d/2
    from math import pi
    
    A = pi*(r**2)
    price = x/A

    print "The price of the pizza, per square inch, is €",price

main()
