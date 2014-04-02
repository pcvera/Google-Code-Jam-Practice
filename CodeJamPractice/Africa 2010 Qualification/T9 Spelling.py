# success in small and large sample inputs

alpha = "abcdefghijklmnopqrtuvwxy"

alphaNum = {}
alphaMod = {}


for idx in range(len(alpha)):
    num = 2 + (idx - (idx%3))/3
    alphaNum[ alpha[idx] ] = str(num)   
    alphaMod[alpha[idx]] = (idx%3) + 1

alphaNum[" "] = "0"
alphaMod[" "] = 1
alphaNum["s"] = "7"
alphaMod["s"] = 4

alphaNum["z"] = "9"
alphaMod["z"] = 4

print alphaNum
print alphaMod

def main():
    f = open("C:\Users\Peter\Downloads\C-large-practice.in", "r")
    
    n = int(f.readline())
    o = open("C:\Users\Peter\Desktop\C-large-practice.out", "w")
    
    for x in range(n):
        output(x+1, process(f.readline()[:-1]), o)

def process(line):
    lastKey = ""
    commands = ""
    print line
    for char in line:
        
        if alphaNum[char] == lastKey:
            commands = commands + " "
            lastKey = ""
        num = alphaNum[char]
        times = alphaMod[char]
        lastKey = num
        commands = commands + num * times
    return commands


def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()