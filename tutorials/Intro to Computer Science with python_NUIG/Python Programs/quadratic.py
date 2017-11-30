# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates the use of the math library.
#    Note: this program crashes if the equation has no real roots.

import math  # makes the math library available

def main():
    print "This program finds the real solutions to a quadratic"
    print

    a, b, c = input("Please enter the coefficients (a, b, c): ")

    discriminant = math.sqrt(b*b - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)

    print
    print "The solutions are:", root1, root2

main()
