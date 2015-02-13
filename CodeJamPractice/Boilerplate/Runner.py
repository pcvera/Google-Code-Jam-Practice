#import re #regex
#import math #math
# math.sqrt(x) -> squre root of x
# math.pow(x, y) -> x ^ y
# math.ceil(math.sqrt(a))


inFile = "B-large-practice"
def main():
    f = open("C:\Users\Peter\Downloads\\" + inFile + ".in", "r")    
    o = open("C:\Users\Peter\Desktop\\" +inFile + ".out", "w")
    
    
    n = int(f.readline())

    for x in range(n):
        output(x+1, process(f.readline()[:-1]), o)

def process(line):
    x = line[:-1].split(" ")
    x.reverse()
    return " ".join(x)


def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()