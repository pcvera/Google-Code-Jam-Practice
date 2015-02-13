from CodeJamHelper import CodeJamHelper

def main():
    h = CodeJamHelper("A-large-practice")    
    
    n = h.nextInt()

    for x in range(n):
        nFlavors = h.nextInt()
        nCustomers = h.nextInt()
        customers = []
        for c in range(nCustomers):
            cValues = h.nextLineOfInts()
            if cValues[0] != (len(cValues)-1)/2:
                print "problem, incorrect number of shake preferences"
            customers.append(cValues[:1])
        if len(customers) != nCustomers:
            print "problem, incorrect number of customers"
        h.output(process(nFlavors, customers))

def process(nFlavors, customers):
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