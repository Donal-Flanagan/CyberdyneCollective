# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():

    # print an introduction.
    print "This program calculates the future value"
    print "of a 10-year investment."

    # input the principal and apr.
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate (as a decimal): ")

    #  repeat 10 times 
    for i in range(10):

        # calculate new principal
        principal = principal * (1 + apr)

    # output final principal
    print "The value in 10 years is:", principal

main()
