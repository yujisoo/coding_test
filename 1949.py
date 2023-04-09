import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
cost = [0]+list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(a):
    visited[a] = 1
    dp[a][1] += cost[a] 
    for i in tree[a]:
        if visited[i]==0:
            dfs(i)
            dp[a][1] += dp[i][0] 
            dp[a][0] += max(dp[i][0], dp[i][1])

dfs(1)
print(max(dp[1]))