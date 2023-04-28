import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,input().split())

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    parent[x] = y
    return

for _ in range(m):
    how, a, b = map(int,input().split())
    if how == 0:
        union(a, b)
    else:
        a1 = find(a)
        b1 = find(b)
        if a1==b1:
            print("YES")
        else:
            print("NO")

