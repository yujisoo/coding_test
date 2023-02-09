n = int(input())
data = [[0,0] for _ in range(n)]
dp = [0]*(n+1)

for i in range(n):
    a,b = map(int,input().split())
    data[i]=[a,b]

for i in range(n):
    for j in range(i+data[i][0],n+1):
        if dp[j]<dp[i]+data[i][1]:
            dp[j] = dp[i]+data[i][1]


print(dp)
print(max(dp))