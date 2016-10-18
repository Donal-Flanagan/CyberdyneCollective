# spherejanuary
# a program to calculate the volume and surface area of a sphere
#
# by Dónal

def print_introduction():
    print 'This is a program to calculate the volume of a sphere'
    print 'of given radius and height.'

def get_radius_and_height():
    r=input('Please enter the radius of your sphere in metres:')
    h=input('Please enter the height of your sphere metres:')
    return r,h

def calculate_surface_area(r,h):
    from math import pi
    A=4*pi*(r**2)*1.0
    return A

def calculate_volume(r,h):
    from math import pi
    V=(4/3)*pi*(r**3)*1.0
    return V

def print_results(A,V):
    print 'The volume of your sphere is ',V,'metres cubed and'
    print 'the surface area of your sphere is ',A,'metres squared.'

def main():
    print_introduction()
    r,h=get_radius_and_height()
    A=calculate_surface_area(r,h)
    V=calculate_volume(r,h)
    print_results(A,V)

if __name__=='__main__':main()
