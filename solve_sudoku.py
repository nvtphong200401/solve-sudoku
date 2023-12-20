class Arc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.domain = set(Domain)
        
    
    def reduceDomain(self, board: list[list[int]]) -> bool:
        
        clonedDomain = set(self.domain)
        for item in clonedDomain:
            if not checkValid(board, self.x, self.y, str(item)):
                self.domain.remove(item)
        
        return len(self.domain) > 0
    
    def __str__(self) -> str:
        return f"domain: {self.domain}"

Domain = {1,2,3,4,5,6,7,8,9}
Arcs = []

def setUpArcs(board):
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == ".":
                arc = Arc(i, j)
                arc.reduceDomain(board)
                Arcs.append(arc)

def reOrder():
    Arcs.sort(key=lambda arc: len(arc.domain))

def solve(board):
    setUpArcs(board)
    reOrder()
    for arc in Arcs:
        print(arc)




def checkValid(board, i, j, num):
    subboard = getSubboard(board, i, j)
    return checkRowOrColValid(board[i], num) and checkRowOrColValid([board[j][i] for j in range(len(board))], num) and checkSubboard(subboard, num)

def checkRowOrColValid(line, num):
    my_set = set()
    for item in line:
        if num in line:
            return False
        else:
            my_set.add(item)
    return True
def checkSubboard(subboard, num):
    n = len(subboard)
    subboard_set = set()
    for i in range(n):
        for j in range(n):
            if num in subboard_set:
                return False
            else:
                subboard_set.add(subboard[i][j])
    return True

def getSubboard(board, row, col):
    row = row // 3
    col = col // 3
    return [[board[i][j] for j in range(col*3, col*3+3)] for i in range(row*3, row*3 +3)]

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

solve(board)
