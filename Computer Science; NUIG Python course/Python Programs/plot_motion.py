# Program: plot_motion.py

from graphics import *
from math import *

from motion import One_d_motion

def main():

    win = GraphWin("Motion of a Particle", 650, 650)
    win.setCoords(-20.0,-20.0,20.0,20.0)

    # Draw the interface.

    Text(Point(-3,-15), "Enter initial posn, and velocity: x,v:").draw(win)
    input1 = Entry(Point(8,-15),3)
    input1.setText("10")
    input1.draw(win)
    input3 = Entry(Point(12,-15),3)
    input3.setText("0")
    input3.draw(win)

    # Draw in the (x,y) axes.

    line1 = Line(Point(-20,0),Point(20,0))
    line2 = Line(Point(0,-14),Point(0,20))
    line1.draw(win)
    line2.draw(win)

    button = Text(Point(0,-18),"Start the Simulation")
    button.draw(win)
    Rectangle(Point(-5,-19),Point(5,-17)).draw(win)

    # Wait for a mouse click.
    
    win.getMouse()

    # Change the button.

    button.setText("Simulation in Progress")

    # Get the initial position and velocity of the particle from the inputs.

    x_pos = eval(input1.getText())
    x_vel = eval(input3.getText())

    # t_final is the time up to which the particle's orbit is tracked.
     
    t_final = 40.0 

    # The time-step is fixed to a given small value.

    dt = 0.005

    N = int(t_final/dt)

    # Create a Motion object.
    
    motion1 = One_d_motion(x_pos,x_vel)

    # Plot the orbit of the motion.

    for i in range(N):
                            
#  The way it's set up below, it plots (x(t),v(t)). However, if you
#  comment out the current p and q, and uncomment the other p and q,
#  it'll plot (t,x(t)).

        p = Point(motion1.get_pos(),motion1.get_vel())

#        p = Point(motion1.get_t(),motion1.get_pos())
        
        motion1.update(dt)
        
        q = Point(motion1.get_pos(),motion1.get_vel())

#        q = Point(motion1.get_t(),motion1.get_pos())
        
        l = Line(p,q)
        l.draw(win)

    # Change the button.

    button.setText("Quit")

    # Wait for click and then quit.

    win.getMouse()
    win.close()
    
main()
