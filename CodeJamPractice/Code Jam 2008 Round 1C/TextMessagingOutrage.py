# success in small and large sample inputs

from CodeJamHelper import CodeJamHelper

def main():
    h = CodeJamHelper("A-large-practice")    
    
    n = h.nextInt()

    for x in range(n):
        pkl = h.nextLineOfInts()
        p = pkl[0]
        k = pkl[1]
        l = pkl[2]
        freq = h.nextLineOfInts()
        h.output(process(p, k , l , freq))

def process(p, k , l , freq):
    freq.sort()
    freq.reverse()
    total = 0
    for idx in range(len(freq)):
        presses = idx / k + 1
        print presses
        total += presses * freq[idx]
    return total
    

if __name__ == "__main__":
    main()