# epact.py
# a program to calculate the value of the epact
# by Dónal

def main():
    print "This program calculates the value of the epact for a given year."

    year = input("Enter a four digit value for a specific year")
    c = year/100
    epact = (8 + (c/4) - c +((8*c+13)/25)+11*(year%19))%30

    print "The epact for ",year ," was",epact

main()
