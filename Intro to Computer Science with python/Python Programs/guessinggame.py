# guessinggame.py
# a program to operate a 'Guess My Number' game
#
# by Dónal Flanagan


def decision(N):
    decision=raw_input('Would you like to play again? (y or n):')
    if decision=="y":
        return main()
    elif decision=="n":
        print 'Goodbye!'
    else:
        print 'Invalid input.'
        decision(N)

def function(N):
    x = input('What is your guess?:')

    if x<N:
        print 'Too low. Try again.'
        return function(N)
    elif x>N:
        print 'Too high. Try again.'
        return function(N)

    elif x==N:
        print 'Excellent! you guessed the number!'
        return decision(N)

        
def main():
    import random
    N=random.randint(1,1000)

    print 'I have a number between 1 and 1000.'
    print 'Can you guess my number?'

    n=function(N)
    

main()
