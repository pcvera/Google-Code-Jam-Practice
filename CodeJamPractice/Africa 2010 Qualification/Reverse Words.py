# success in small and large sample inputs

def main():
    f = open("C:\Users\Peter\Downloads\B-large-practice.in", "r")
    
    n = int(f.readline())
    o = open("C:\Users\Peter\Desktop\B-large-practice.out", "w")
    
    for x in range(n):
        output(x+1, process(f.readline()), o)

def process(line):
    x = line[:-1].split(" ")
    x.reverse()
    return " ".join(x)


def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()