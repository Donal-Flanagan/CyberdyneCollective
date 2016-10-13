max = 13  # total number of projects to choose from

def choose3(n):
    a = (n*n + n - 1117) %  max + 1
    b = (n*n + n - 1123) % (max - 1) + 1
    c = (n*n + n - 1129) % (max - 2) + 1
    if a > b:
        a, b = b, a
    else:
        b = b + 1
    if a > c:
        a, c = c, a
    else:
        c = c + 1
    if b > c:
        b, c = c, b
    else:
        c = c + 1
    return a, b, c
    

def main():
    id = raw_input("Enter your student id: ")
    print "\nStudent ID %s: " % (id)    
    print "Choose two projects from %d, %d, and %d.\n" % choose3(int(id)/10)

main()
    
