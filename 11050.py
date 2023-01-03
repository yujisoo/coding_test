n,k = map(int,input().split())
ans = 1
for i in range(n-k+1,n+1):
    ans *= i
for i in range(1,k+1):
    ans /= i
print(int(ans))