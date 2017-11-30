#  $Id: futval_graph.py,v 1.2 2006/10/27 14:17:31 goetz Exp $

# download the graphics library from
#
#   http://mcsp.wartburg.edu/zelle/python/graphics.py
#
from graphics import *

def main():

    # introduction
    print "This program plots the growth of a 10-year investment."

    # get user data
    principal = input("Enter the initial principal: ")
    apr = input("Enter the Annual Percentage Rate: ")

    # creat a graphics window with labels.
    win = GraphWin("Investment Growth Chart 2006", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20,  80), ' 7.5K').draw(win)
    Text(Point(20,  30), '10.0K').draw(win)

    # draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for successive years
    for year in range(10):
        raw_input("Press <Enter> to continue")
        principal = principal * (1 + apr)
        xll = 25 * year + 65
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # finalize
    raw_input("Press <Enter> to quit")
    win.close()

main()
