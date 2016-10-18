# cylinder.py
# a program to calculate the volume and surface area of a cylinder
#
# by Dónal

def main():
    from math import pi
    print 'This program will calculate the volume and'
    print 'surface area of a given cylinder.'

    r = input('Please enter the radius of the cylinder in metres:')
    h = input('Please enter the height of the cylinder in metres:')

    V = pi*(r**2)*h*1.0
    A = (2*pi*r)*(r+h)*1.0

    print 'The volume of this cylinder is',V,'metres cubed'
    print 'and the surface area of this cylinder is',A,'metres squared.'

main()
