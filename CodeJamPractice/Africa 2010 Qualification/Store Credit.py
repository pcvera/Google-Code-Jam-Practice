# success in small and large sample inputs

def main():
    f = open("C:\Users\Peter\Downloads\A-large-practice.in", "r")
    
    n = int(f.readline())
    o = open("C:\Users\Peter\Desktop\A-large-practice.out", "w")
    
    for x in range(n):
        c = int(f.readline())
        i = int(f.readline())
        p = [int(y) for y in  f.readline().split(" ")]
        output(x+1, process(c, i, p), o)
        
def process(c, i, p):
    priceSet = {}
    for x in p:
        if x not in priceSet:
            priceSet[x] = 1
        else:
            priceSet[x]= priceSet[x] + 1
    for index in range(len(p)):
        x = p[index]
        if c - x in priceSet and (x != c-x or priceSet[x] > 1):
            return "" + str(index+1) + " " + str(index +1 + p[index+1:].index(c-x)+1)


    
def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()