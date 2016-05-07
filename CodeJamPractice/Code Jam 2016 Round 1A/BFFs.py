import os

def main():
    #generate()
    h = CodeJamHelper("B-practice")

    n = h.nextInt()

    for x in range(n):
        numKids = h.nextInt()
        l = h.nextLineOfInts()
        h.output(process(l))


def process(line):
    m = createAdjMatrix(line)
    inv = invertAdjMatrix(m)
    loners = findEdgesNobodyLikes(inv, len(line))
    infl = findInflections(m)

    return findAllChains(m, loners)

def findAllChains(m, loners):
    mLoners = [x for x in loners]
    visited = {}
    out = []
    while len(visited) < len(m):
        mKeys = [x for x in m.keys()]
        chain = []
        if len(mLoners) == 0:
            curr = mKeys[0]
        else:
            curr = loners[0]
        print "starting with " + str(curr)

        while m[curr] in mKeys:
            visited[curr] = True
            mKeys.remove(m[curr])
            chain.append(m[curr])
            curr = m[curr]
        out.append(chain)
    return out







def createAdjMatrix(line):
    out = {}
    for idx in range(len(line)):
        out[idx+1] = line[idx]
    return out

def invertAdjMatrix(m):
    out = {}
    for x in m:
        if x not in out:
            out[x] = []
        out[x].append(x)
    return out

def findEdgesNobodyLikes(m, nKids):
    out = []
    for x in range(1, nKids):
        if x not in m:
            out.append(x)
    return out

def findInflections(m):
    out = {}
    for k in m:
        if k == m[m[k]]:
            s = [k, m[k]]
            s.sort()
            out[s[0]] = s[1]
    return out


class CodeJamHelper:
    """Helper for the common things I do during Google Code Jam"""
    def __init__(self, baseFileName):
        self.ensureDirectory("./output")
        self.inFile = open("./input/" + baseFileName + ".in", "r")
        self.outFile = open("./output/" + baseFileName + ".out", "w")
        self.caseNum = 1

    def ensureDirectory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def output(self, value):
        print "Case #" + str(self.caseNum) + ": " + str(value)
        self.outFile.write( "Case #" + str(self.caseNum) + ": " + str(value) + "\n")
        self.caseNum = self.caseNum + 1

    def nextLine(self):
        return self.inFile.readline()[:-1] #strip the new line, it's bad

    def nextInt(self):
        return int(self.nextLine())

    def nextLineOfInts(self, delim=" "):
        line = self.nextLine()
        return [int(x) for x in line.split(delim)]

    def nextLineOfFloats(self, delim=" "):
        line = self.nextLine()
        return [float(x) for x in line.split(delim)]

    def nextDelimitedLine(self, delim=" "):
        return self.nextLine().split(delim)

    def nextDelimitedMatrix(self, x, y, delim=" "):
        matrix = []
        for _ in range(len(x)):
            line = self.nextLine()
            line = [item for item in line.split(delim)]
            if(len(line) != y):
                print "problem, matrix does not match specified dimensions"
            matrix.append(line)
        return matrix

    def nextCharMatrix(self, x, y):
        matrix = []
        for _ in range(len(x)):
            line = self.nextLine()
            line = [item for item in line]
            if(len(line) != y):
                print "problem, matrix does not match specified dimensions"
            matrix.append(line)
        return matrix

    def getStringMatrix(self, matrix, space=True):
        out = ""
        for line in matrix:
            out = out + "\n"
            for item in line:
                out = out + str(item)
                if(space):
                    out = out + " "
            if(space):
                out = out[:-1]
        return out

if __name__ == "__main__":
    main()
