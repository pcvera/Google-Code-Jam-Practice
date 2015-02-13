# success in small and large sample inputs
# fun one

def main():
    f = open("C:\Users\Peter\Downloads\B-large-practice.in", "r")
    o = open("C:\Users\Peter\Desktop\B-large-practice.out", "w")
    
    n = int(f.readline()[:-1])
    
    for i in range(n):
        xy = f.readline()[:-1];
        x = int(xy.split(" ")[0])
        y = int(xy.split(" ")[1])
        map = []
        for j in range(x):
            line = f.readline()[:-1]
            line = [int(l) for l in line.split(" ")]
            if len(line) != y:
                print "problem"
            map.append(line)
        output(i+1, process(map), o)
        
def process(map):
    print stringmap(map)
    adj = {}
    for x in range(len(map)):
        for y in range(len(map[0])):
            point = (x, y)
            adj[point] = adjacentFlow(map, x, y)
            
    emptiesTo = {}
    for x in range(len(map)):
        for y in range(len(map[0])):
            visited = []
            current = (x,y)
            if current not in emptiesTo:
                next = adj[current]
                visited.append(current)

                while next != current:
                    current = next
                    next = adj[current]
                    visited.append(current)

                    if next in emptiesTo:
                        next = emptiesTo[next]
                        current = next
                for z in visited:
                    emptiesTo[z] = next
    output = []
    letterMap = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(map)):
        outLine = []
        for y in range(len(map[0])):
            point = emptiesTo[(x,y)]
            if point not in letterMap:
                letterMap[point] = alphabet[0]
                alphabet = alphabet[1:]
            outLine.append(letterMap[point])
        output.append(outLine)
    return stringmap(output)

adjPoints = [(-1, 0),(0,-1),(0,1),(1,0)]
def adjacentFlow(map, x, y):
    lowest = map[x][y]
    lowPoint = (0,0)
    for point in adjPoints:
        if between(x + point[0], 0, len(map)) and between(y+point[1], 0, len(map[0])):
            if lowest > map[x + point[0]][y + point[1]]:
                lowest = map[x + point[0]][y + point[1]]
                lowPoint = point
            
    return (x + lowPoint[0], y + lowPoint[1])

pointDirs = {}
pointDirs[-1,0] = "^"
pointDirs[0,-1] = "<"
pointDirs[1,0] = "v"
pointDirs[0,1] = ">"
pointDirs[0,0] = "."

def printAdjMatrix(map, adj):
    out = ""
    for x in range(len(map)):
        out = out + "\n"
        for y in range(len(map[0])):
            point = (x,y)
            dir = (adj[point][0]-x, adj[point][1] - y)
            out = out + pointDirs[dir]
            out = out + " "
    print out


def between(x, low, high):
    return x >= low and x < high
    

def stringmap(map):
    out = ""
    for line in map:
        out = out + "\n"
        for item in line:
            out = out + str(item) +" "
        out = out[:-1]
    return out


def output(case, outline, o):
    print "Case #" + str(case) + ":" + str(outline)
    o.write( "Case #" + str(case) + ":" + str(outline) + "\n")
    
if __name__ == "__main__":
    main()