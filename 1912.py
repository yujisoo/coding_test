import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

for i in range(1,n):
    data[i]=max(data[i-1]+data[i],data[i])
print(max(data))