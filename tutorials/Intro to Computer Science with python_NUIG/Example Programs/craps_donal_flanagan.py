# craps_donal_flanagan.py
# a program to simulate a game of craps
#
# By Dónal Flanagan 06665268

from random import randrange

def Intro():
    # Prints an introduction explaining the function of the program
    print "This is a program which simulates a game of craps."
    print "The player rolls 2 dice. If the player rolls a 7 or"
    print "an 11 they win. If they roll a 2,3 or 12 they lose."
    print "Otherwise they roll again until they roll a 7, to"
    print "lose, or their initial roll again, to win."

def play():
    n = input("How many times would you like to play?:")
   # for i in range(n):
    #    wins,losses=roll()
    return n

    
def simdice():
    
    roll2 = randrange(1,7) + randrange(1,7)
    return roll2

def roll():#sim 1 game
    roll1 = randrange(1,7) + randrange(1,7)
    
    if roll1 ==2 or 3 or 12:
        outcome = "loss"
    elif roll1 == 7  or roll1 ==11:
        outcome = "win"

    elif roll1 == 11:
        wins = wins + 1
    else:
        outcome = roll_for_point()
    return outcome

def roll_for_point(roll1):
#    roll2 = randrange(1,7) + randrange(1,7)
    simdice()
    while not (roll2 != 7 or roll1):
        simdice()
    if roll2 == roll1:
        outcome = "win"
    else:
        outcome = "loss"

    return outcome

def ngames(n):
    wins =0
    for i in range(n):
        outcome = roll()
        if outcome == "win":
            wins = wins+1
    return wins

def score(wins,losses):
    print "You won",wins,"times and lost",losses,"times."
    wins *100/n

def main():
    Intro()
    play()
    n = play()
    score(n,wins)

if __name__ == "__main__": main()
