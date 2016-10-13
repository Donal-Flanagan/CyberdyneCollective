# THIS WON'T WORK UNTIL AFTER YOU'VE DONE QUESTION 2.

# Program: plot_planetary_motion

from graphics import *
from math import pi

# YOU NEED TO CREATE CLASS Planet AND SAVE IT IN planetary_motion.py

# from planetary_motion import Planet

def main():

    win = GraphWin("Planetary Motion", 650, 650)
    win.setCoords(-20.0,-20.0,20.0,20.0)

    # Draw the interface.

    Text(Point(-3,-15), "Enter initial posn, and velocity: x,y,vx,vy:").draw(win)
    input1 = Entry(Point(8,-15),3)
    input1.setText("6")
    input1.draw(win)
    input2 = Entry(Point(10,-15),3)
    input2.setText("0")
    input2.draw(win)
    input3 = Entry(Point(12,-15),3)
    input3.setText("0")
    input3.draw(win)
    input4 = Entry(Point(14,-15),4)
    input4.setText("2")
    input4.draw(win)

    # Draw an orange circle representing the Sun

    circle1 = Circle(Point(0,0),0.25)
    circle1.setOutline('orange')
    circle1.setFill('orange')
    circle1.draw(win)

    button = Text(Point(0,-18),"Start the Simulation")
    button.draw(win)
    Rectangle(Point(-5,-19),Point(5,-17)).draw(win)

    # Wait for a mouse click.
    
    win.getMouse()

    # Change the button.

    button.setText("Simulation in Progress")

    # Get the initial position and velocity of the planet from the inputs.

    x_pos = eval(input1.getText())
    y_pos = eval(input2.getText())
    x_vel = eval(input3.getText())
    y_vel = eval(input4.getText())

    # t is the time up to which the planet's orbit is tracked.
     
    t = 4.0*pi*(x_pos**2+y_pos**2)**1.5/(39.3**0.5) 

    # The time-step is fixed to a given small value.
 
    dt = 0.001

    N = int(t/dt)

    # Create a Planet object.
    
    planet1 = Planet(x_pos,y_pos,x_vel,y_vel)

    # Plot the orbit.

    for i in range(N):
                            
        p = Point(planet1.x_pos,planet1.y_pos)
        planet1.update(dt)
        q = Point(planet1.x_pos,planet1.y_pos)
        l = Line(p,q)
        l.draw(win)

    # Change the button.

    button.setText("Quit")

    # Wait for click and then quit.

    win.getMouse()
    win.close()


    
class Planet:


    def __init__(self,xp, yp, xv, yv):
        self.x_pos = xp
        self.y_pos = yp
        self.x_vel = xv
        self.y_vel = yv
        self.mu = 39.3

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def get_x_vel(self):
        return self.x_vel

    def get_y_vel(self):
        return self.y_vel


    def update(self, dt):
        x_pos_new = self.x_pos+dt*self.x_vel
        y_pos_new = self.y_pos+dt*self.y_vel
        x_vel_new = self.x_vel+dt*self.__f1(self.x_pos,self.y_pos)
        y_vel_new = self.y_vel+dt*self.__f2(self.x_pos,self.y_pos)

        self.x_pos = x_pos_new
        self.y_pos = y_pos_new
        self.x_vel = x_vel_new
        self.y_vel = y_vel_new


    def __f1 (self,xp, yp):
        return (-(self.mu)*self.x_pos)/(((self.x_pos**2.0)+(self.y_pos**2))**1.5)

    def __f2 (self,xp, yp):
        return (-(self.mu)*self.y_pos)/(((self.x_pos**2.0)+(self.y_pos**2))**1.5)

 

    
main()

    
