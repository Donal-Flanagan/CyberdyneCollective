# triangle.py
# a program to draw a triangle
#
# by Dónal

from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5), "Click on 3 points")
    message.draw(win)


    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("red")
    triangle.setOutline("black")
    triangle.draw(win)


    message.setText("Click anywhere to exit")
    win.getMouse()
    win.close()

main()
