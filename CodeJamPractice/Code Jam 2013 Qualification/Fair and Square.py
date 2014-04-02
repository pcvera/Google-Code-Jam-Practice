# success in small and large-1 sample inputs but not large-2

import math


def main():
    f = open("C:\Users\Peter\Downloads\C-large-practice-1.in", "r")
    
    n = int(f.readline())
    o = open("C:\Users\Peter\Desktop\C-large-practice-1.out", "w")
    
    
    for x in range(n):
        line = [int(y) for y in f.readline()[:-1].split(" ")]
        a = line[0]
        b = line[1]
        output(x+1, process(a, b), o)
        
def process(a, b):
    #print str(a) + " < x < " + str(b)
    return countStaticPalindromes(a,b)   

#sufficient for small input
#def process(a, b):
#    squares = []
#    print str(a) + " < x < " + str(b)
#    curr = int(math.ceil(math.sqrt(a)))
#    while curr <= math.sqrt(b):
#        if isPalindrome(curr):
#            squares.append(curr * curr);
#        curr = curr + 1
#    return len([x for x in squares if isPalindrome(x)])

def isPalindrome(num):
    string = str(num)
    return checkPalindrome(string)

def checkPalindrome(num):
    if len(num) == 0:
        return True
    elif num[0] == num[-1]:
        return checkPalindrome(num[1:-1])
    else:
        return False


def countStaticPalindromes(a, b):
    #print [sq for sq in allSquares if sq >= a and sq <= b]
    return len([sq for sq in allSquares if sq >= a and sq <= b])

#written for large dataset 1
allSquares = []
x = 1
dist = 3
while x <= math.sqrt(math.pow(10, 14)):
    if(isPalindrome(x)):
        if(isPalindrome(x * x)):
            #print str(x) + " * " + str(x) + " = " + str(x * x)
            allSquares.append(x*x)
    x = x + 1
    if(x > 10 and str(x)[0] == "4"):#via http://mathforum.org/library/drmath/view/51510.html
        x = x * 10/4


#boilerplate
def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()