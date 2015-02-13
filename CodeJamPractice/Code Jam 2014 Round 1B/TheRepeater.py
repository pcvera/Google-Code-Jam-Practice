from CodeJamHelper import CodeJamHelper
import math

def main():
    h = CodeJamHelper("A-small-attempt1")    
    
    t = h.nextInt()
    for x in range(t):
        n = h.nextInt()
        strs = []
        for y in range(n):
            strs.append(h.nextLine())
        h.output(process(strs))

def process(strs):
    if not validate(strs):
        return "Felga Won"
    
    counts = [count(s) for s in strs]
    sums = [sum([x[y] for x in counts]) for y in range(len(counts[0]))]
    averages = [round(1.0 * y / len(strs)) for y in sums]
    edits = [[math.fabs(averages[x] - c[x]) for x in range(len(c))] for c in counts]
    return int(sum( [item for sublist in edits for item in sublist]))
def validate(t):
    strs = [characterize(s) for s in t]
    return all(x == strs[0] for x in strs)

def count(s1):
    s = s1[:] #copy
    counts = []
    curr = s[0]
    count = 0
    while(len(s) != 0):
        if(curr == s[0]):
            count = count + 1
        else:
            counts.append(count)
            curr = s[0]
            count = 1
        s = s[1:]
    counts.append(count)
    return counts

def characterize(str):  
    s = str[:] #copy
    o = s[0]
    while(len(s) != 0):
        if(s[0] != o[-1]):
            o = o + s[0]
        s = s[1:]
    return o
    

if __name__ == "__main__":
    main()