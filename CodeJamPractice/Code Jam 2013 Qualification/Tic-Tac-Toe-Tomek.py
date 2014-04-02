# success in small and large sample inputs

def main():
    f = open("C:\Users\Peter\Downloads\A-large-practice.in", "r")
    
    n = int(f.readline())
    o = open("C:\Users\Peter\Desktop\A-large-practice.out", "w")
    
    for c in range(n):
        board = []
        board.append([x for x in f.readline()[:-1]])
        board.append([x for x in f.readline()[:-1]])
        board.append([x for x in f.readline()[:-1]])
        board.append([x for x in f.readline()[:-1]])
        f.readline()
        output(c+1, process(board), o)

def process(board):
    for horiz in board:
        print horiz
        if homogeneous(horiz):
            return homogeneousChar(horiz) + " won"
    for idx in range(4):
        if homogeneous([x[idx] for x in board]):
            return homogeneousChar([x[idx] for x in board]) + " won"
    forwardDiag = [board[0][0], board[1][1], board[2][2], board[3][3]]
    if homogeneous(forwardDiag):
        return homogeneousChar(forwardDiag) + " won"
    revDiag = [board[0][3], board[1][2], board[2][1], board[3][0]]
    if homogeneous(revDiag):
        return homogeneousChar(revDiag) + " won"
    
    for horiz in board:
        if "." in horiz:
            return "Game has not completed"
    return "Draw"


def homogeneousChar(line):
    return line[0] if line[0] != "T" else line[1]

def homogeneous(line):
    char = line[0] if line[0] != "T" else line[1]
    opposite = "X" if "O" == char else "O"
    return not opposite in line and not "." in line
    
    

def output(case, outline, o):
    print "Case #" + str(case) + ": " + str(outline)
    o.write( "Case #" + str(case) + ": " + str(outline) + "\n")
    
if __name__ == "__main__":
    main()