import sys
input = sys.stdin.readline

n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    if i == 1:
        dp[i][0]+=dp[0][0]
        dp[i][1]+=dp[0][0]
    else:
        for j in range(i+1):
            if j == 0:
                dp[i][j]+=dp[i-1][j]
            elif j==i:
                dp[i][j]+=dp[i-1][j-1]
            else:
                dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])
                
print(max(dp[n-1]))