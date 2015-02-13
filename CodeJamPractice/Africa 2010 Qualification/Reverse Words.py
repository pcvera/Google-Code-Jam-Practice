# success in small and large sample inputs

from CodeJamHelper import CodeJamHelper

def main():
    h = CodeJamHelper("B-large-practice")    
    
    n = h.nextInt()

    for x in range(n):
        h.output(process(h.nextDelimitedLine()))

def process(line):
    line.reverse()
    return " ".join(line)

if __name__ == "__main__":
    main()