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
    # Gets a value fo rthe amount of games of craps to be played
    n = input("How many times would you like to play?:")
    return n

def simdice():
    # A simulation for the dice throw, i found it easier to just call it for
    # the second throw.
    roll2 = randrange(1,7) + randrange(1,7)
    return roll2

def roll():
    # The initial dice throw, i thought it would be simpler not to use the
    # simdice function here.
    roll1 = randrange(1,7) + randrange(1,7)
    
    # This defines whether the player wins or loses with the initial roll
    if roll1 ==2 or roll1 == 3  or roll1 == 12:
        outcome = "loss"
    elif roll1 == 7  or roll1 ==11:
        outcome = "win"
    # Calling the roll for point function    
    else:
        outcome = roll_for_point(roll1)
    
    return outcome

def roll_for_point(roll1):
    # This function runs the roll for point part of the game
    roll2  = simdice()
    while not(roll2 == 7 or roll2 == roll1):
    # Here we use simdice() to roll indefinately until a winning or losing roll
        roll2 = simdice()
    if roll2 == roll1:
        outcome = "win"
    else:
        outcome = "loss"
    return outcome

def ngames(n):
    # This function runs the roll() function however many times were specified in
    # the play function.
    wins = 0
    losses = 0
    for i in range(n):
        outcome = roll()
        if outcome == "win":
            wins = wins + 1
        else:
            losses = losses + 1
    return wins,losses

def score(n,wins,losses):
    # A function to print the results of the game
    print "After ",n,"games, you have won ",wins," times and lost ",losses," times."
    print "The probability that you will win at craps is: ",(wins*1.0)/n,"."

def main():
    Intro()
    n = play()
    wins,losses = ngames(n)
    score(n,wins,losses)

if __name__ == "__main__": main()

