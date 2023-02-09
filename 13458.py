n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
ans = 0
for i in range(len(a)):
    if a[i]>=b:
        a[i]-=b
    
        if a[i]%c==0:
            ans += a[i]//c
        else:
            ans += a[i]//c+1
print(ans+len(a))