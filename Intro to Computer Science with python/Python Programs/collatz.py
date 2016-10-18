# collatz.py
# by Dónal

def main():
    n=input("Please input the number you want computed:")

    sequence=[n]
    while n!=1:
        if n%2==0:
            n=n/2
            sequence.append(n)

        elif n%2!=0:
            n=(3*n)+1
            sequence.append(n)

    print sequence
    print len(sequence)

main()
