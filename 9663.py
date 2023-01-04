n = int(input())
board = [0]*n
cnt = 0

def check(a):
    for i in range(a):
        if board[a]==board[i] or abs(board[a]-board[i]) == a-i:
            return False
    return True

def queen(a):
    global cnt
    if a == n :
        cnt+=1
    else:
        for i in range(n):
            board[a] = i
            if check(a):
                queen(a+1)
queen(0)
print(cnt) 

    
    
