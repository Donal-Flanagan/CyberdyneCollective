# random_Dónal_Flanagan.py
# Dónal Flanagan 06665268

from random import randrange
import math


def start():
    print "This is a program to simulate a random walk of N steps, m times."
    N = input("How many steps do you want the walk to last?:")
    m = input("How many times do you want to repeat the program?:")
    return N,m

def sim_one_walk(N):
    Dn = 0.0

    for i in range(N):
        x = randrange(1,3)
        if x == 1:
            Dn = Dn - 1.0
        else:
            Dn = Dn + 1.0
    return Dn

def simulate_m_walks(m,N):
    sumSq = 0
    dist = 0
    for i in range(m):
        Dn = sim_one_walk(N)
        dist = dist + abs(Dn)
        sumSq = sumSq + Dn**2
    return dist, sumSq

def results(m,dist,sumSq):
    meandistance = dist/m
    rms = sqrt(sumSq/m)

    print "The root mean square distance is ",meandistance," and the mean"
    print "distance travelled from the starting point is ",dist,"."

def main():
    N,m = start()
    dist, sumSq = sim_m_walks(m,N)
    results(m,dist,sumSq)

main()
