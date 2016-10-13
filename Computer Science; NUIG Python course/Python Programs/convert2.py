# convert2.py
#
# a program to convert Fahrenheit into Celsius
# by Dónal

def main():
    print "This program converts degrees Fahrenheit to degrees Celsius."
    fahrenheit = input("What is the temperature in degrees Fahrenheit?")
    celsius = (fahrenheit - 32) * (5.0/9.0)
    print "the temperature in degrees Celsius is", celsius, "degrees Celsius."
main()
