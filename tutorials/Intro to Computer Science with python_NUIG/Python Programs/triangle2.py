# triangle.py

def  square(x):
    return x*x

from math import sqrt

def distance(p1, p2):
    dist = sqrt(square(p1.getX() - p2.getX()) + square(p1.getY()-p2.getY()))
    return dist

from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText("The perimeter is %0.2f" % (perim))

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
    
    
