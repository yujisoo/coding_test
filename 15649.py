from itertools import permutations

n,m = map(int,input().split())
a = [i for i in range(1,n+1)]

ans = list(permutations(a,m))
for i in ans:
    print(*i)