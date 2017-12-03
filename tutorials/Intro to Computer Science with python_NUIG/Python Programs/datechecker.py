# datechecker.py
# a program to check if a given date is valid
#
# by Dónal

def leapyear(z):
    if z%4 == 0:
        if z%100==0 and z%400!=0:
            return 0
            
        else:
            return 1

    else:
        return 0

def main():
    x,y,z = input("Please input a date in the form day,month,year:")

    if z>-1:
        if y in [9,4,6,11]:
            if 0<x<=30:
                print "Valid date."
            else:
                print "Invalid date."

        elif y == [1,3,5,7,8,10,12]:
            if 0<x<=31:
                print "Valid date."
            else:
                print "Invalid date."

        elif leapyear(z)==0 and y == 2:
            if 0<x<=28:
                print "Valid date."
            else:
                print "Invalid date."

        elif leapyear(z)==1 and y==2:
            if  0<x<=29:
                print "valid date"
            else:
                print "Invalid date."

main()
