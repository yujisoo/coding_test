import copy,sys
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
maps = []
dice = [0,0,0,0,0,0]

for i in range(n):
    a = list(map(int,input().split()))
    maps.append(a)

d = list(map(int,input().split()))

def move(d,dice):
    tmp = copy.deepcopy(dice)
    if d == 1:
        tmp[0] = dice[3]
        tmp[2] = dice[0]
        tmp[3] = dice[5]
        tmp[5] = dice[2]
    elif d == 2:
        tmp[0] = dice[2]
        tmp[2] = dice[5]
        tmp[3] = dice[0]
        tmp[5] = dice[3]
    elif d == 3:
        tmp[0] = dice[4]
        tmp[1] = dice[0]
        tmp[4] = dice[5]
        tmp[5] = dice[1]
    else:
        tmp[0] = dice[1]
        tmp[1] = dice[5]
        tmp[4] = dice[0]
        tmp[5] = dice[4]
   
    return tmp

for i in d:
    if i == 1:
        if 0<=y+1<m:
            y +=1
            dice = move(i,dice)
            if maps[x][y]!=0:
                dice[-1] = maps[x][y]
                maps[x][y] = 0
            else:
                maps[x][y] = dice[-1]
            print(dice[0])
    elif i == 2:
        if 0<=y-1<m:
            y -=1
            dice = move(i,dice)
            if maps[x][y]!=0:
                dice[-1] = maps[x][y]
                maps[x][y] = 0
            else:
                maps[x][y] = dice[-1]
            print(dice[0])
    elif i == 3 :
        if 0<=x-1<n:
            x -=1
            dice = move(i,dice)
            if maps[x][y]!=0:
                dice[-1] = maps[x][y]
                maps[x][y] = 0
            else:
                maps[x][y] = dice[-1]
            print(dice[0])
    else:
        if 0<=x+1<n:
            x +=1
            dice = move(i,dice)
            if maps[x][y]!=0:
                dice[-1] = maps[x][y]
                maps[x][y] = 0
            else:
                maps[x][y] = dice[-1]
            print(dice[0])
                