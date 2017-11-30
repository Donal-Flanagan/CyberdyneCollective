# gradespercent.py
# a program to calculate the grades of a test
#
# by Dónal

def main():
    n = input("Please input the percentage mark:")
    if 100>=n>=90:
        print "A"
    elif 89>=n>=80:
        print "B"
    elif 79>=n>=70:
        print "C"
    elif 69>=n>=60:
        print "D"
    elif n<60:
        print "F"
main()
