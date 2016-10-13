# grades.py
# a program to grade quiz scores
#
# by Dónal

def main():
    n = input("please input the quiz score you want graded:")

    if n == 5:
        print "A"
    elif n==4:
        print "B"
    elif n==3:
        print"C"
    elif n==2:
        print "D"
    elif n>=5:
        print "This score is too large."
    else:
        print "F"
    
main()
