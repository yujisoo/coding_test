import sys
input = sys.stdin.readline

n, m = map(int,input().split())
card = list(map(int,input().split()))

a = 0
ans = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = card[i]+card[j]+card[k]
            if a<=m:
                ans = max(a,ans)
print(ans)