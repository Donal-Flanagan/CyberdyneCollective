# rball.py
#   Simulation of a racquetball game. Illustrates use of random
#       numbers and functions to implement top-down design.

from random import random

def main():
    printIntro()
    probA, probB, n, m = getInputs()
    matchesA,matchesB = simNmatches(n,m,probA,probB)
    printSummary(matchesA, matchesB)

def printIntro():
    # Prints an introduction to the program
    print "This program simulates a game of racquetball between two"
    print 'players called "A" and "B".  The abilities of each player is'
    print "indicated by a probability (a number between 0 and 1) that"
    print "the player wins the point when serving. Player A always"
    print "has the first serve.\n"

def getInputs():
    # Returns probA, probB, number of games to simulate
    a = input("What is the prob. player A wins a serve? ")
    b = input("What is the prob. player B wins a serve? ")
    n = input("How many matches to simulate? ")
    m = input("The winner of each match is the best out of \nhow many games?(this should be an odd number):")
    return a, b, n, m
    

def simNmatches(n,m,probA,probB):
    matchesA = matchesB = 0
    for i in range(n):
        winsA,winsB = simOnematch(m,probA,probB)
        if winsA>=((m+1)/2):
            matchesA = matchesA + 1
        else:
            matchesB = matchesB + 1
    return matchesA, matchesB   
       

def simOnematch(m, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    matchesA = matchesB = 0
    for i in range(m):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game of racquetball between two players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if random()<0.5:
            serving == "A"
            if random() < probA:
                scoreA = scoreA + 1
        else:
            serving = "B"
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # Returns true if game is over, false otherwise
    return a == 15 or b == 15

def printSummary(matchesA, matchesB):
    # Prints a summary of wins for each player.
    m = matchesA+matchesB
    print "\nMatches simulated:", m
    print "Matches won by A: %d (%0.1f%%)" % (matchesA, float(matchesA)/m*100)
    print "Matches won by B: %d (%0.1f%%)" % (matchesB, float(matchesB)/m*100)

if __name__ == "__main__": main()





