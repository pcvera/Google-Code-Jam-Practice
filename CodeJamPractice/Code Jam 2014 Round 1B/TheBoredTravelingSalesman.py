from CodeJamHelper import CodeJamHelper
from sets import Set

def main():
    h = CodeJamHelper("C-sample")    
    
    t = h.nextInt()
    for x in range(t):
        nm = h.nextLineOfInts()
        n = nm[0]
        m = nm[1]
        zips = []
        flights = []
        for cities in range(n):
            zips.append(h.nextInt())
        for f in range(m):
            s = h.nextLineOfInts()
            flight = (s[0], s[1])
            flights.append(flight)
        h.output(process(zips, flights, h))

            
            


def process(zips, flights, h):
    #zips = [0] + (zips)
    print zips
    
    visited= dfs(createAdjMatrix(len(zips), flights), findWeights(zips), findPriority(zips), 0,Set([0]), [0])
    visited = visited[1:]
    visited.reverse()
    return "".join(str(zips[item-1]) for item in visited)
    

def dfs(matrix, costs, priorities,source, visited, orderVisited=[0]):
    n = neighbors(matrix, source, priorities)
    for neighbor in n:
        if neighbor not in visited:
            visited.add(neighbor)
            orderVisited.append(neighbor)
            dfs(matrix, costs, priorities, neighbor, visited, orderVisited)
    return orderVisited
   

def neighbors(matrix, source, priorities):
    n = []
    for x in priorities:
        if matrix[source][x]:
            n.append(x)
    return n
    
    
def createAdjMatrix(l, edges):
    adj = []
    for x in range(l+1):
        adj.append([False]*(l+1))
    for x in range(l+1):
        adj[0][x] = True
        adj[x][0] = True
    
    for edge in edges:
        adj[edge[0]][edge[1]] = True
        adj[edge[1]][edge[0]] = True
    return adj

def findWeights(zips):
    
    zCopy = zips[:]
    zCopy.sort()
    p = []
    for idx in range(len(zips)):
        p.append(zCopy.index(zips[idx]))
    return p
    
    
def findPriority(zips):
    zCopy = zips[:]
    zCopy.sort()
    p = []
    for idx in range(len(zips)):
        p.append(zips.index(zCopy[idx])+1)
    p.reverse()
    return p
    

if __name__ == "__main__":
    main()