from collections import deque
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
m,n = map(int,input().split())
maps = [[]for _ in range(m)]
dp = [[-1]*n for i in range(m)]

for _ in range(m):
    maps[_] = (list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(a,b):
    if a == m-1 and b == n-1:
        return 1
    if dp[a][b] == -1:
        dp[a][b] = 0
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[nx][ny]<maps[a][b]:
                dp[a][b] += dfs(nx,ny)

    return dp[a][b]
               
print(dfs(0,0))