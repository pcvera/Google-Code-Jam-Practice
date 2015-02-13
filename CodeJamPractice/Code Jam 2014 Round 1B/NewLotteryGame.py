from CodeJamHelper import CodeJamHelper
import math

def main():
    h = CodeJamHelper("B-sample")    
    
    t = h.nextInt()
    for x in range(t):
        abk = h.nextLineOfInts()
        a = abk[0]
        b = abk[1]
        k = abk[2]
        h.output(process(a,b,k))

def process(a,b,k):
    for x in range(a):
        for y in range(b):
            print str(x) + " & " + str(y)+ " = " + str(x & y)
            print bin(x) + " & " + bin(y)+ " = " + bin(x & y)
    return str(a) + " " + str(b) + " " + str(k)
    

if __name__ == "__main__":
    main()