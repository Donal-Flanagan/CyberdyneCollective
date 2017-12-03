# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():

    # print an introduction.
    print "This program calculates the future value"
    print ;"of a 10-year investment."

    # input the principal, yearly rate and number of times the rate is compounded per year.
    principal = input("Enter the initial principal: ")
    rate = input("Enter the yearly rate (as a decimal): ")
    periods = input("Enter the no of times interest is compounded per year: ")

    #  repeat 10 times 
    for i in range(10*periods):

        # calculate new principal
        principal = principal * (1 + (rate/periods))

    # output final principal
    print "The value in 10 years is:", principal

main()

