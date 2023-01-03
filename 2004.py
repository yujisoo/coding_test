import sys
input = sys.stdin.readline

def two(n):
    a = 0
    while n != 0:
        n = n//2
        a += n
    return a

def five(n):
    a = 0
    while n != 0:
        n = n//5
        a += n
    return a

n,m = map(int,input().split())
ans = min(two(n)-two(m)-two(n-m),five(n)-five(m)-five(n-m)) 
print(ans)