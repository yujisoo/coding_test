from collections import deque
import sys
input = sys.stdin.readline

n,m =map(int,input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(a,b,visit,now,cnt):
    global answer
    visit[a][b]=1
    if now == 4:
        answer = max(answer,cnt)
        return 0
    for i in range(4):
        nx = dx[i]+a
        ny = dy[i]+b
        if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
            if now == 2:
                visit[nx][ny] = 1
                dfs(a,b,visit,now+1,cnt+maps[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx,ny,visit,now+1,cnt+maps[nx][ny])
            visit[nx][ny]= 0
visit = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visit[i][j]=1
        dfs(i,j,visit,1,maps[i][j])
        visit[i][j]=0
print(answer)
