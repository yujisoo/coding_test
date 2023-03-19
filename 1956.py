import sys
input = sys.stdin.readline

v,e = map(int,input().split())
inf = 10000 * v + 1
dis = [[inf]*(v+1) for i in range(v+1)]
r = []
for _ in range(e):
    a,b,c = map(int,input().split())
    dis[a][b] = c
for i in range(1,v+1):
    for j in range(1,v+1):
        for k in range(1,v+1):
            dis[j][k] = min(dis[j][k],dis[j][i]+dis[i][k])
ans = inf
for i in range(1,v+1):
    ans = min(ans,dis[i][i])
if ans == inf:
    print(-1)
else:
    print(ans)
