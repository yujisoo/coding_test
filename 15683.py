import sys,copy
input = sys.stdin.readline

n,m = map(int,input().split())
maps = []
q = []
for i in range(n):
    input_data = list(map(int,input().split()))
    maps.append(input_data)
    for j in range(m):
        if input_data[j] in [1,2,3,4,5]:
            q.append([i,j,input_data[j]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

def cctv(maps,mm,x,y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==0:
                    maps[nx][ny]=7
                elif maps[nx][ny]==6:
                    break
                else:
                    continue
            else:
                break
ans = int(1e9)

def dfs(maps,cnt):
    global ans
    
    if cnt == len(q):
        c = 0
        for i in range(n):
            c += maps[i].count(0)
        ans = min(ans,c)
        return
    tmp = copy.deepcopy(maps)
    x, y, mo = q[cnt]
    for i in mode[mo]:
        cctv(tmp,i,x,y)
        dfs(tmp,cnt+1)
        tmp = copy.deepcopy(maps)

dfs(maps,0)
print(ans)