# easter2.py
# by Dónal



def main():
    y = input("Please input a year between 1900 and 2099:")

    a=y%19
    b=y%4
    c=y%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    No=22+d+e
    Na=No-31
    Nb=No-7
    Nc=Na-7

    if 1900>y or y>2099:
        print "Date not valid."

    if 1900<=y<=2099:
        if y ==1954 or y==1981 or y==2049 or y==2076:
            if No<=31:
                print "Easter is on March ",Nb,"."
            if No>31:
                print "Easter is on March ",Nc,"."

        else:
            if No<=31:
                print "Easter is on March ",No,"."
            if No>31:
                print "Easter is on March ",Na,"."

main()
