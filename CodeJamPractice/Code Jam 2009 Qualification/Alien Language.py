# success in small and large sample inputs
import re

def main():
    f = open("C:\Users\Peter\Downloads\A-large-practice.in", "r")
    
    o = open("C:\Users\Peter\Desktop\CodeJam2009Qual\A-large-practice.out", "w")
    
    l = f.readline()[:-1]
    l = l.split(" ")
    d = int(l[1])
    n = int(l[2])
    l = int(l[0])
    
    dictionary = []
    for x in range(d):
        dictionary.append(f.readline()[:-1])
    
    for x in range(n):
        output(x+1, process(f.readline()[:-1], dictionary), o )

def process(line, dict):
    count = 0
    line = line.replace("(", "[")
    line = line.replace(")", "]")
    for x in dict:
        if re.match(line, x):
            count = count + 1
    return count

def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()