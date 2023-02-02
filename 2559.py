n, k = map(int,input().split())
num = list(map(int,input().split()))
data = [0]

for i in num:
    data.append(i+data[-1])
    
ans = data[k]
for i in range(1,n-k+1):
    ans = max(ans,data[i+k] - data[i])
print(ans)