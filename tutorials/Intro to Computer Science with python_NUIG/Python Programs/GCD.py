# GCD.py
# by Dónal

def main():
    n,m=input("Please input two numbers in the form 'x,y':")

    while m!=0:
        n,m=m,n%m

    print "The Greatest Common Divider is ",n,"."

main()
