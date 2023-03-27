from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
x,y,size = 0,0,2
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            x = i
            y = j

def bfs(a,b,s):
    visit = [[0]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    q = deque()
    q.append((a,b))
    visit[a][b] = 1
    tmp = []

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                if maps[nx][ny]<=s:
                    q.append((nx,ny))
                    visit[nx][ny] = 1
                    distance[nx][ny] = distance[x][y]+1
                    if maps[nx][ny]<s and maps[nx][ny] !=0:
                        tmp.append([nx,ny,distance[nx][ny]])
    return sorted(tmp,key=lambda x : (-x[2],-x[0],-x[1]))


cnt = 0
result = 0
while True:
    s = bfs(x,y,size)
    if len(s) == 0:
        break
    nx,ny,dist = s.pop()

    result+=dist
    maps[x][y] = 0
    maps[nx][ny] = 0
    x,y = nx,ny
    cnt+=1
    if cnt == size:
        size+=1
        cnt = 0
print(result)