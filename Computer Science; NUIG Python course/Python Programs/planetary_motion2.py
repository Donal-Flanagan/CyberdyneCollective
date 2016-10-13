# Program: planetary_motion.py

from math import *

def main():
    print_introduction()
    r,h = get_radius_and_height()
    cylinder1 = Cylinder(r,h)
    A = cylinder1.surface_area()
    V = cylinder1.volume()
    print_results(A,V)

class Cylinder:

    def __init__(self,r,h):
        self.radius = r
        self.height = h

    def surface_area(self):
        return 2*pi*(self.radius**2)+2*pi*self.radius*self.height

    def volume(self):
        return pi*(self.radius**2)*self.height

def print_introduction():
    print "This program calculates the surface area and volume of a cylinder"
    print "The radius and height of the cylinder are input by the user"
    print " "

def get_radius_and_height():
    radius = input("What is the radius of the cylinder (in metres)?")
    height = input("What is the height of the cylinder (in metres)?")
    print " "
    return radius, height

def print_results(surface_area,volume):
    print "The surface area of the cylinder is ", surface_area," metres squared."
    print "The volume of the cylinder is ", volume," metres cubed."

if __name__=='__main__':main()
