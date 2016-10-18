# BMI.py
# A program to calculate a persons body mass index and
# tell them whether they are healthy enough.
#
# by Dónal

def main():
    w,h = input("Please enter your weight in pounds and your height in inches:")

    BMI = (w*703)/(h**2)

    if BMI>25:
        print "Your BMI is ",BMI," which is above the healthy range."

    elif 25>=BMI>=19:
        print "Your BMI is ", BMI," which is perfectly healthy."

    elif BMI<19:
        print "Your BMI is ", BMI,"which is below the healthy range."

main()
