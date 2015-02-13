#import re #regex
#import math #math
# math.sqrt(x) -> squre root of x
# math.pow(x, y) -> x ^ y
# math.ceil(math.sqrt(a))
from decimal import *

inFile = "B-small-attempt2 (1)"
def main():
    f = open("C:\Users\Peter\Downloads\\" + inFile + ".in", "r")    
    o = open("C:\Users\Peter\Desktop\\" +inFile + ".out", "w")
    
    
    n = int(f.readline())

    for x in range(n):
        output(x+1, process(f.readline()[:-1]), o)

def process(line):
    x = [float(y) for y in line[:-1].split(" ")]
    c = x[0]
    f = x[1]
    x = x[2]
    bestTime = timeTil(x, f, 0)
    factoryBuys = []
    factoryBuyTime = 0
    
    n = 0
    factoryTime = 0
    baseTime = timeTil(x,f, 0)
    while baseTime > factoryTime + timeTil(c,f,n) + timeTil(x, f, n+1):
        baseTime = factoryTime + timeTil(c,f,n) + timeTil(x, f, n+1)
        factoryTime = timeTil(c,f,n) + factoryTime
        n = n + 1
    baseTime = round(baseTime, 7)
    end = str(baseTime) + "0000000"[len(str(baseTime).split(".")[1]):]

    return end
    #print  + sum(factoryBuys)
    
def timeTil(x, f, n):
    return x / (f*n + 2)
    

def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()