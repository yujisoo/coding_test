s1 = list(input())
s2 = list(input())
dp = [[0]*(len(s2)) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            if i==0 or j==0:
                dp[i][j]+=1
            else:
                dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])