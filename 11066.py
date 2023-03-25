import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    file = list(map(int,input().split()))
    dp = [[0]*(k+1) for i in range(k+1)]

    for i in range(k-1):
        dp[i][i+1] = file[i]+file[i+1]
        for j in range(i+2,k):
            dp[i][j] = dp[i][j-1]+file[j]

    for i in range(2,k):
        for j in range(k-i):
            n = i+j
            dp[j][n] += min([dp[j][a] + dp[a+1][n] for a in range(j,n)])
            
    print(dp[0][k-1])