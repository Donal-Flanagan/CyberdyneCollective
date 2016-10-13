# draws_a_polygram.py
# it draws a polygram..... duh
#
# by Dónal


from graphics import *

def main():
    win = GraphWin("Draws A Polgram",400,400)
    label = Text(Point(200,380),"Click on five points.")
    label.draw(win)
    
    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    p4 = win.getMouse()
    p4.draw(win)

    p5 = win.getMouse()
    p5.draw(win)

    poly = Polygon(p1,p2,p3,p4,p5)
    poly.setFill("purple")
    poly.setOutline("orange")
    poly.draw(win)


    
    return p1,p2,p3,p4,p5

    c=Point((p1+p2+p3+p4+p5)/5)


    message.setText(c,"A Purple Polygon")

    
    rect = Rectangle(Point(100,350),Point(300,360))
    message.setText("Click Here To Quit")
    win.getMouse()
    win.close()

main()
