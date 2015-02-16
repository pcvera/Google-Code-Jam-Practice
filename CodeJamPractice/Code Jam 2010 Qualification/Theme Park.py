from CodeJamHelper import CodeJamHelper

import math

#sufficient for large and small inputs

def main():
    h = CodeJamHelper("C-large-practice")    
    
    t = h.nextInt()

    for x in range(t):
        params = h.nextLineOfInts(" ")
        groups = h.nextLineOfInts(" ")
        if len(groups) != params[2]:
            print "problem"
        h.output(process(params[0], params[1], groups))

def process(rides, capacity, groups):
    #edge cases:
        #more room than possible groups can fill
            #handle by setting max possible groups == len(groups)
        #more room and hit end of list
            #handle by wrapping back to front
    #efficiencies:
        #rides starting from the same position will always produce the same set of riders and amount of money
            #cache these values
            #sufficient for small input without this efficiency
        #when a group is repeated, the loop that brought them to this point will be repeated indefinitely
        #until the total rides are used
            #use math to figure out how many times this loop will repeat and how much money it will produce
            #rather than calculating each index every time
#    print rides
#    print capacity
#    print groups
    
    nextGroup = 0
    cash = 0
    maxGroups = len(groups)
    
    moneyCache = {}
    nextGroupCache = {}
    ride = 0
    while ride < rides: #if you use "for ride in range(rides)" syntax, this line takes forever for large numbers
                        #apparently range allocates memory for all of the integers within the range
                        #and xrange is the alternative while below python 3
        remainingCapacity = capacity
        numGroups = 0
        rideCash = 0
        startGroup = nextGroup
        if startGroup in nextGroupCache:
            #this block is where I started doing efficiency stuff for the large input
            ridesInLoop, moneyInLoop = sumLoop(startGroup, moneyCache, nextGroupCache) 
            if ridesInLoop < rides - ride:
                loops = (rides - ride) / ridesInLoop
                ride += ridesInLoop * loops -1
                rideCash = moneyInLoop * loops 
            else:
                nextGroup = nextGroupCache[startGroup]
                rideCash = moneyCache[startGroup]
        else:
            while remainingCapacity >= groups[nextGroup] and numGroups < maxGroups:
                remainingCapacity -= groups[nextGroup]
                rideCash += groups[nextGroup]
                nextGroup += 1
                nextGroup %= maxGroups
                numGroups += 1
            moneyCache[startGroup] = rideCash
            nextGroupCache[startGroup] = nextGroup
        cash += rideCash
        ride += 1
    return cash

def sumLoop(start, moneyCache, nextGroupCache):
    totalMoney = moneyCache[start]
    totalRides = 1
    current = nextGroupCache[start]
    while current != start:
        totalMoney = totalMoney + moneyCache[current]
        totalRides = totalRides + 1
        current = nextGroupCache[current]
    return totalRides, totalMoney
    

if __name__ == "__main__":
    main()
