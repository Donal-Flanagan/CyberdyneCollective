# futvalplusyears.py
#    A program to compute the value of an investment.

def main():

    # print an introduction.
    print "This program calculates the future value"
    print "of an investment."

    # input the principal,apr and number of years invested.
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate (as a decimal): ")
    years = input("Enter the no of years to invest for: ")

    #  repeat 10 times 
    for i in range(years):

        # calculate new principal
        principal = principal * (1 + apr)

    # output final principal
    print "The value in", years, "years is:", principal

main()

