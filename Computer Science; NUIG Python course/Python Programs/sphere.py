# sphere.py
# aprogram to calculate the volume and surface area of a given sphere
#
# by Dónal

def main():
    from math import pi
    r = input("Enter the radius of the sphere:")
    x = pi

    V = (4/3)*x*(r**3)
    A = 4*x*(r**2)

    print "The volume of the sphere is", V
    print "and the surface area of the sphere is", A

main()
