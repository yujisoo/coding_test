import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
data = [0]

for i in num:
    data.append(i+data[-1])

for _ in range(m):
    a,b = map(int,input().split())
    ans = data[b]-data[a-1]
    print(ans)