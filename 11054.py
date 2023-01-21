n = int(input())
s = list(map(int,input().split()))
s_re = list(reversed(s))

dp1 = [0]*n
dp2 = [0]*n
for i in range(n):
    for j in range(i):
        if s[i]>s[j] and dp1[i]<dp1[j]:
            dp1[i]=dp1[j]
        if s_re[i]>s_re[j] and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]
    dp1[i]+=1
    dp2[i]+=1
dp2 = list(reversed(dp2))
a = 0
for i in range(n):
    a = max(a,dp1[i]+dp2[i]-1)
print(a)