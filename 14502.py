import sys,copy
input = sys.stdin.readline
from itertools import combinations
from collections import deque

ans = 0
maps = []
n,m = map(int,input().split())
for i in range(n):
    maps.append(list(map(int,input().split())))
virus = []
room = []
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            room.append([i,j])
        if maps[i][j]==2:
            virus.append([i,j])

a = list(combinations(room,3))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def safe(a1,b,c):
    q = deque()
    q.append((a1,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if c[nx][ny] == 0:
                    c[nx][ny] = 2
                    q.append((nx,ny))
            else:
                continue


for wall in a:
    b = copy.deepcopy(maps)
    for i in range(3):
        b[wall[i][0]][wall[i][1]]=1
    for i in virus:
        safe(i[0], i[1], b)
        cnt = 0
        for ta in range(n):
            for tb in range(m):
                if b[ta][tb]==0:
                    cnt+=1   
    ans=max(ans,cnt)

print(ans)