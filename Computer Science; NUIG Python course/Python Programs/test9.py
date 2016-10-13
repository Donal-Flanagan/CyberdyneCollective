# -*- coding: cp1252 -*-
# random_Dónal_Flanagan.py
# Dónal Flanagan 06665268

# The first comment is there because I was having problems with some kind of bug in the python system.
# I changed the name of the program and put in that piece of code as it said to do in the window that
# kept popping up. I have no idea why it suddenly started working when I did that and neither does the lab
# technician who is helping us.

from random import randrange
from math import *

# Here i just bunched the print_intro and get_input functions in together
def start():
    print "This is a program to simulate a random walk of N steps, m times."
    N = input("How many steps do you want the walk to last?:")
    m = input("How many times do you want to repeat the program?:")
    return N,m

# This is my simulation of each walk
def sim_one_walk(N):
    Dn = 0.0

    for i in range(N):
        x = randrange(1,3)
        if x == 1:
            Dn = Dn - 1.0
        else:
            Dn = Dn + 1.0
    return Dn

# Here I did the main part of the program, repeating the walk m times and getting values for the
# absolute values of all the distances added together (dist) and all the distances squared and added
# (sumSq). These will be used in the results function to calculate values for the mean distance and
# the root mean square distance.
def sim_m_walks(m,N):
    sumSq = 0.0
    dist = 0.0
    for i in range(m):
        Dn = sim_one_walk(N)
        dist = dist + abs(Dn)
        sumSq = sumSq + Dn**2
    return dist, sumSq

# Here I calculated the mean distance walked and the root mean square distance and then printed them.
def results(m,dist,sumSq):
    meandistance = dist/m
    rms = sqrt(sumSq/m)

    print "The root mean square distance is",rms,"and the mean"
    print "distance travelled from the starting point is",meandistance,"."

# This is just the main function where I combined all the other functions.
def main():
    N,m = start()
    dist, sumSq = sim_m_walks(m,N)
    results(m,dist,sumSq)

main()
    
