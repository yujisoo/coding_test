import sys
input = sys.stdin.readline

n = int(input())

# n에 따른 각 자리수가 맨 뒤에 올 경우를 저장
dp = [[0]*10 for _ in range(101)]

# n=1이면 1-9가 가능
for i in range(1,10):
    dp[1][i] = 1

# 대각선 방향으로 더해준다
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%1000000000)