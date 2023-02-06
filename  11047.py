import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = [0]*n
for _ in range(n):
    coin[_]=(int(input()))

cnt = 0

coin = reversed(coin)
for i in coin:
    cnt += k//i
    k -= (k//i) * i

print(cnt)