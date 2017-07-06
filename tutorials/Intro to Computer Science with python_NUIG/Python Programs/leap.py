# leapyear.py
# a program to calculate whether or not a year is a leap year
#
# by Dónal

def leapyear(year):
    if year%4 == 0:
        if((year%100==0) & (year%400==0)):
            print "This is a leap year."
        else:
            print "This is not a leap year."

    else:
        print "Thsi is not a leap year."

main()
