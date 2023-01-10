import sys
input= sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int,input().split())))

diff = 1000
visit=[False]*n

def dfs(depth,idx):
    global diff
    if depth==n//2:
        start=0
        link=0
        for i in range(n):
            for j in range(n):
                if visit[i]==True and visit[j]==True:
                    start+=s[i][j]
                elif visit[i]==False and visit[j]==False:
                    link+=s[i][j]
        diff = min(diff,abs(link-start))
        if diff == 0:
            print(0)
            exit(0)
        return
    for i in range(idx,n):
        if visit[i]==False:
            visit[i]=True
            dfs(depth+1,i+1)
            visit[i]=False
dfs(0,0)
print(diff)