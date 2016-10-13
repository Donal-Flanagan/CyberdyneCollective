# convert.py
#
# a program to convert Fahrenheit into Celsius.
# by Susan

'''
Created on 6 Nov 2015

@author: donal
'''

if __name__ == '__main__':
    celsius = int(input("What is the temperature in degrees Celsius? "))
    fahrenheit = (9.0 / 5.0) * celsius + 30
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

