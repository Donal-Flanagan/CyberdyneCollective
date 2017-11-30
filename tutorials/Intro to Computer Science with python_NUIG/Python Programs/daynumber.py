# daynumber.py
# by Dónal

def leapyear(y):
    if y%4 == 0:
        if y%100==0 and y%400!=0:
            return 0
            
        else:
            return 1

    else:
        return 0
    
def main():
    d,m,y= input("Please input the date in the form 'day,month,year':")

    x = 31*(m-1)+d
    n = x-(4*m+23)/10
    z = n+1

    if leapyear(y)==0:
        if m<3:
            print x

        else:
            print n

    else:
        if m <3:
            print x
        else:
            print z

main()
        

    
        
