# Program: motion_dónal_flanagan
# Dónal Flanagan
# 06665268

from math import *

class One_d_motion:


    def __init__(self, pos, vel):
        """This is the constructor function of the module. The initial position (pos),"""
        """ and velocity (vel) need to be input and it will return the these same values"""
        """into the class, along with an initial value for t, the time(-20.0)."""
        self.pos = pos
        self.vel = vel
        self.t = -20.0

    def get_pos(self):
        """This function will return the position of the particle."""
        return self.pos

    def get_vel(self):
        """ This function will return the velocity of the particle"""
        return self.vel
    
    def get_t(self):
        """This function will return the length of time over which the movement will be plotted"""
        return self.t

    def update(self, dt):
        """This function will update the position and velocity of the particle as the time changes."""
        
        pos_new = self.pos+dt*self.vel
        vel_new = self.vel+dt*self.__f(self.pos,self.vel,self.t)
        t_new = self.t + dt
 
        self.pos = pos_new
        self.vel = vel_new
        self.t = t_new

    def __f(self,x,v,t):
        """This function defines the value for __f the force which is used in the formulae in the update function."""
        return -x
