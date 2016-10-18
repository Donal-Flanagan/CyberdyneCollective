# maybe.py
# a program which tells the user if an integer is positive, negative or zero
#
# by Dónal

def main():
    print 'This program will tell you if an integer is positive, negative or'
    print 'equal to zero.'
    x=input('Please input the integer you wish to compute:')

    if x==0:
        print 'This integer is zero.'

    elif x>0:
        print 'This integer is positive.'

    else:
        print 'This integer is negative.'

main()
