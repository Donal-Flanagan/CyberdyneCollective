# degreedays.py
# by Dónal

def main():
    name=raw_input("What file are the numbers in?:")
    temp = open(name, 'r')

    h=0
    c=0

    for line in temp:
        line = int(line)
        if line<60:
            h=h+(60-line)

        elif line>80:
            c=c+(line-80)

    print h," heating degree days."
    print c," cooling degree days."

main()
