# convert4.py
#
# a program to convert Feet and Inches into Centimetres
# by Dónal

def main():
    print "A program to convert Feet and Inches into Centimetres"
    feet, inches = input("What is the distance in Feet and Inches?")
    centimetres = (feet * 30) + (inches * 2.5)
    print "The distance in centimetres is", centimetres, "cm."

main()
