# month.py
#print a month's abbreviation

def main():

    # lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = input("month number (1-12)")
    pos = (n - 1)*3


    abbrev = months[pos:pos+3]
    print "The month is ", abbrev + "."

main()
    
