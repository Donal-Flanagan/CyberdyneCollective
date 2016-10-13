# dateconvert.py
#  converts a date in the form 'dd/mm/yyyy' to 'month day, year'

import string

def main():

    # get the date
    date = raw_input("Enter a date (dd/mm/yyyy): ")

    # split into components  
    day, month, year = string.split(date, "/")


    # convert month number to name

    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    month = months[eval(month) - 1]

    #  output the date in new format
    print "The converted date is:", month, day + ",", year

main()
