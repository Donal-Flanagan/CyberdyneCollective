# tax.py
# a program to calculate the amount of tax payable by the user
#
# by Dónal

def main():
    x=input('Please enter your annual income:')

    if x<20000:
        print 'There is no tax due.'

    else:
        y=x-20000*1.0

        if y<=20000:
            t=y*0.3
            print 'There is €',t,' tax due.'

	elif 20000<y<60000:
            z=y-20000

            a=20000*.3
            b=z*.4
            t=a+b
            print 'There is €',t,' tax due.'

        elif y>60000:
            z=y-60000
            a=20000*.3
            b=40000*.4
            c=z*.5
            t=a+b+c
            print 'There is €',t,' tax due.'

main()
