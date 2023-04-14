import sys,heapq
input = sys.stdin.readline

n = int(input())
meet = []
dp = [0]*(n+1)

for i in range(n):
    a,b = map(int,input().split())
    meet.append([a,b])
cost = 0

for i in range(n):
    cost = max(cost,dp[i])
    if i+meet[i][0] > n:
        continue
    dp[i+meet[i][0]] = max(cost+meet[i][1],dp[i+meet[i][0]])

print(max(dp))
    