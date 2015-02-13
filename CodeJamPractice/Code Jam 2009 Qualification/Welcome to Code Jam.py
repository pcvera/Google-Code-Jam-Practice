#sufficient for small practice, insufficient for large
inFile = "C-small-practice"
def main():
    f = open("C:\Users\Peter\Downloads\\" + inFile + ".in", "r")    
    o = open("C:\Users\Peter\Desktop\\" +inFile + ".out", "w")
    
    
    n = int(f.readline())

    for x in range(n):
        output(x+1, process(f.readline()[:-1]), o)

def process(line):
    print line
    base = "welcome to code jam"
    stripped = "".join([x for x in line if x in base])
    searchStr, countArr = countRelevant(stripped)
    count = doCount(base, searchStr, countArr)
    return padNumber4(count)
    
def doCount(base, searchStr, countArr):
    if base == "":
        return 1
    let = base[0]
    idx = searchStr.find(let)
    count = 0
    while idx != -1:
        count = count + countArr[idx] * doCount(base[1:], searchStr[idx + 1 :], countArr[idx + 1 :])
        idx = searchStr.find(let, idx + 1)
    return count

def padNumber4(num):
    nStr = str(num)
    if len(nStr) > 4:
        return nStr[:-4]
    else:
        return "0000"[len(nStr):] + nStr

def countRelevant(s):
    if len(s) == 0:
        return "", []
    curr = s[0]
    count = 1
    outs = ""
    outa = []
    for x in s[1:]:
        if(curr != x):
            outs = outs + curr
            outa.append(count)
            curr = x
            count = 0
        count = count + 1
    outs = outs + curr
    outa.append(count)

    return outs, outa
    
    
def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()