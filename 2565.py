n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key = lambda x:x[0])
dp = [0]*(n)
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1
print(n-max(dp))