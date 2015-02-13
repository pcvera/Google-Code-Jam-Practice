#sufficient for large and small practice
#needed to look at contest discussion to find this solution
#need to work on my dynamic programming


inFile = "C-large-practice"
def main():
    f = open("C:\Users\Peter\Downloads\\" + inFile + ".in", "r")    
    o = open("C:\Users\Peter\Desktop\\" +inFile + ".out", "w")
    
    
    n = int(f.readline())

    for x in range(n):
        output(x+1, process(f.readline()[:-1]), o)

def process(line):
    dMatrix = []
    base = "elcome to code jam"
    dMatrix.append(countW(line))
    for c in base:
        currLine = [0]
        for idx in range(len(line)):
            x = line[idx]
            if x == c:
                currLine.append(dMatrix[-1][idx] + currLine[-1])
            else:
                currLine.append(currLine[-1])
        dMatrix.append(currLine)
    return padNumber4(dMatrix[-1][-1])

def padNumber4(num):
    nStr = str(num)
    if len(nStr) > 4:
        return nStr[-4:]
    else:
        return "0000"[len(nStr):] + nStr

def countW(line):
    c = 0
    counts = [0]
    for x in line:
        if x == "w":
            c = c + 1
        counts.append(c)
    return counts
    
def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()