# investment.py
# by Dónal

def main():
    initial=input("Please enter the amount to be invested:")
    interest=input("Please enter the interest rate as a percentage:")
    x=initial
    money=0
    years=0

    while initial < (2*x):
       initial = initial + ((initial/100)*interest)
       years=years+1

    print "It will take ",years," years for this investment to double:"

main()
