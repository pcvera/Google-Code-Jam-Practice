from CodeJamHelper import CodeJamHelper

import math

#Sufficient for both large and small inputs

def main():
    h = CodeJamHelper("A-large-practice")    
    
    t = h.nextInt()

    for x in range(t):
        case = h.nextLineOfInts(" ")
        h.output(process(case[0], case[1]))

def process(snappers, snaps):
    """
    Strategy here is to treat the snappers like a n-bit counter where n is the number of snappers
    All snappers be on only if the number of snaps from 0 is equal to 2^n - 1
    2^n snaps resets
    """
    numSnapsForReset = int(math.pow(2, snappers))
    return "ON" if snaps % numSnapsForReset == numSnapsForReset - 1 else "OFF"
    
    

if __name__ == "__main__":
    main()
