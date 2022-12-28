import sys
input = sys.stdin.readline

n = int(input())
data = []
rank = [1]*n
for _ in range(n):
    a,b = map(int,input().split())
    data.append([a,b])

for i in range(n-1):
    for j in range(i+1,n):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            rank[j]+=1
        elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i]+=1
for i in rank:
    print(i,end=' ')