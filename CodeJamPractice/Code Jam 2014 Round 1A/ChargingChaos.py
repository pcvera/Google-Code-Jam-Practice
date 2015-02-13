from CodeJamHelper import CodeJamHelper

def main():
    h = CodeJamHelper("A-small-attempt0")    
    
    t = h.nextInt()

    for x in range(t):
        nt = h.nextLineOfInts()
        n = nt[0]
        t = nt[1]
        flows = h.nextDelimitedLine()
        flows = [[y == "1" for y in flow] for flow in flows ]
        devices = h.nextDelimitedLine()
        devices = [[y == "1" for y in device] for device in devices]
        h.output(process(flows, devices))

def process(flows, devices):
    f = countOnes(flows)
    d = countOnes(devices)
    flips = [0] * len(flows[0])
    
    for x in range(len(f)):
        if f[x] != d[x] and len(flows) - f[x] != d[x]:
            return "NOT POSSIBLE"
        if len(flows) - f[x] == d[x] and f[x] != d[x]:
            flips[x] = 1
        if len(flows) - f[x] == f[x]:
            #case where switches are half and half, need to check flip or not
            flips[x] = -1
    #we have hypothetical flips, need to verify
    flipPoss = genFlips(flips, [[]])
    flipPoss = ["".join([str(x) for x in line]) for line in flipPoss]

    for poss in flipPoss:
        if(testFlip(poss, flows, devices)):
            return countFlip(poss)
    return "NOT POSSIBLE"
        
def countFlip(poss):
    count = 0
    for x in poss:
        if x == "1":
            count = count + 1
    return count

def testFlip(flips, flows, devices):
    newFlows = [x for x in flows]
    newDevices = [x for x in devices]
    for x in range(len(flips)): #perform flips
        for line in newFlows:
            if(flips[x] == "1"):
                line[x] = not line[x]

    newFlows = ["".join(["1" if x else "0" for x in line ]) for line in newFlows]
    newDevices = ["".join(["1" if x else "0" for x in line ]) for line in newDevices]
    newFlows.sort()
    newDevices.sort()
    for x in range(len(newFlows)):
        if newFlows[x] != newDevices[x]:
            return False
    return True

def genFlips(base, outL):
    if len(base) == 0:
        return outL
    if base[0] == -1:
        temp = [[y for y in x] for x in outL] #copy
        for x in outL:
            x.append(0)
        for x in temp:
            x.append(1)
        outL.extend(temp)
    else:
        for x in outL:
            x.append(base[0])
    return genFlips(base[1:], outL)
    
def countOnes(l):
    total = [0]*len(l[0])
    for line in l:
        for x in range(len(l[0])):
            if(line[x]):
                total[x] = total[x] + 1
    return total
        
if __name__ == "__main__":
    main()