from CodeJamHelper import CodeJamHelper

def main():
    h = CodeJamHelper("A-large-practice")    
    
    n = h.nextInt()

    for x in range(n):
        h.output(process(h.nextInt(), h.nextLineOfInts(), h.nextLineOfInts()))

def process(length, line1, line2):
    if(len(line1) != length):
        print "problem, line1 length"
    if(len(line2) != length):
        print "problem, line2 length"
    line1.sort()
    line2.sort()
    total = 0;
    for x in range(len(line1)):
        total = total + line1[x] * line2[-1-x]
    return total
        
if __name__ == "__main__":
    main()