# success in small and large sample inputs

def main():
    f = open("C:\Users\Peter\Downloads\B-large-practice.in", "r")
    
    t = int(f.readline())
    o = open("C:\Users\Peter\Desktop\B-large-practice.out", "w")
    
    for y in range(t):
        measure = f.readline()
        n = int(measure.split(" ")[0])
        m = int(measure.split(" ")[1])
        lawn = []
        for x in range(n):
            row = f.readline()[:-1]
            row = row.split(" ")
            if len(row) != m:
                print "problem"
            lawn.append([int(x) for x in row])
        output(y+1, process(lawn), o)

def process(lawn):
    for x in range(len(lawn)):
        for y in range(len(lawn[0])):
            if not (lineWorks(lawn[x], y) or lineWorks([col[y] for col in lawn], x)):
                return "NO"
    return "YES"
                
    

def lineWorks(line, index):
    return len([x for x in line if x <= line[index]]) == len(line) 


def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()