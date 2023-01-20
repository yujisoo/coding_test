import sys
input = sys.stdin.readline

n = int(input())

grape = [0]*n
idx = [0]*n

for i in range(n):
    grape[i] = int(input())

for i in range(n):
    if i==0:
        idx[i] = grape[0]
    elif i==1:
        idx[i] = grape[0]+grape[1]
    elif i==2:
        idx[i] = max(grape[0]+grape[i],grape[1]+grape[i],idx[i-1])
    else:
        idx[i] = max(grape[i]+idx[i-2],grape[i]+grape[i-1]+idx[i-3],idx[i-1])

print(max(idx))