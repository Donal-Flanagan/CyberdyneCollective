# Loanrepayments.py
# a program to to calculate the repayments on a given loan over a period.
#
# by Dónal Flanagan

def main():
    print 'This program calculates the repayments on a given loan over a period.'
    principal = input('Enter the initial principal:')
    apr = input('Enter the annual interest rate:')
    years = input('Enter the length of time over which the loan is to be repaid in years:')
    periods = input('Enter the number of times the interest is compounded per year:')

    n=years*periods*1.0
    r=(apr/100.0)/periods
    p=principal*1.0

    a=r*((1+r)**n)
    b=((1+r)**n)-1
    x=p*(a/b)
    print '€', x, ' is to be repaid each period.'
main()
