# prime.py
# by Dónal

def main():
    n=input("Please input the number you would like checked:")

    import math

    if n==1:
        print "The number ",n," is a prime number."

    elif n==2:
        print "The number ",n," is a prime number."

    else:
        x=2
        while x<=math.sqrt(n):
            if n%x!=0:
                print "The number ",n," is a prime number."
                return 0
            elif n%x==0:
                print "The number ",n," is not a prime number."
                return 0
            x=x+1 

main()
