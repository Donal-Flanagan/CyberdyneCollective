# convert_gui.py
# a program to convert Celsius to Fahrenheit using
# a simple graphical user interface
# by Dónal

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 300, 240)
    win.setCoords(0.0,0.0,3.0,4.0)

    #Draw the interface

    Text(Point(1,3),"Celsius Temp:").draw(win)
    Text(Point(1,1),"Fahrenheit Temp:").draw(win)

    input = Entry(Point(2,3),5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)

    #Wait for a mouse click
    win.getMouse()

    #Convert input
    celsius = eval(input.getText())
    fahrenheit = 9.0*celsius/5.0+32.0

    #Display output and change button
    output.setText("%0.1f"%fahrenheit)
    button.setText("Quit")

    #Wait for mouse click and then quit
    win.getMouse()
    win.close()


main()
