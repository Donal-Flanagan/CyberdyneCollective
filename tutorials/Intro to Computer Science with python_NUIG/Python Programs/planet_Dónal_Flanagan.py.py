# Program: planetary_motion.py

class Planet:

    """This module contains the formulae used in a program to graph the movement of a planet around the sun"""
    """The variables x_pos, y_pos, x_vel and y_vel need to be passed to the class,these are the initial position"""
    """and velocity of the planet in question as (x,y) coordinates around the sun as an origin. The class will"""
    """return the updated position of the planet after a period of time (dt) and the updated coordinates can be"""
    """used in a graphics module graphing the movement."""
    
    def __init__(self,x_pos, y_pos, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

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
        return (-(39.3)*self.x_pos)/(((self.x_pos**2.0)+(self.y_pos**2))**1.5)

    def __f2 (self,xp, yp):
        return (-(39.3)*self.y_pos)/(((self.x_pos**2.0)+(self.y_pos**2))**1.5)

 
