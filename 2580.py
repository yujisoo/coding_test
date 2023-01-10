import sys
input = sys.stdin.readline
board = []
blank = []
for _ in range(9):
    board.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            blank.append([i,j])


def row(a,find):
    for i in range(9):
        if board[a][i] == find:
                return False
    return True

def col(a,find):
    for i in range(9):
        if board[i][a] == find:
                return False
    return True

def square(a,b,find):
    a1 = a%3
    b1 = b%3
    for i in range(a-a1,a-a1+3):
        for j in range(b-b1,b-b1+3):
            if board[i][j] == find:
                return False
    return True

def dfs(a):
    if a == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)
    for k in range(1,10):
        x = blank[a][0]
        y = blank[a][1]
        if row(x,k) and col(y,k) and square(x,y,k):
            board[x][y]=k
            dfs(a+1)
            board[x][y]=0
dfs(0)