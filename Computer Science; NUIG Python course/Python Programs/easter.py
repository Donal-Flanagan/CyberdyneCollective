# easter.py
# by Dónal

def main():
    y = input("Please input a year between 1982 and 2048:")

    a=y%19
    b=y%4
    c=y%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    No=22+d+e
    Na=No-31

    if 1982>y or y>2048:
        print "Date not valid."

    if 1982<=y<=2048:
        if No<=31:
            print "Easter is on March ",No,"."
        if No>31:
            print "Easter is on March ",Na,"."

main()

    
    
