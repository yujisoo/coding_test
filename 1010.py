from math import factorial

for _ in range(int(input())):
    n,m = map(int,input().split())
    ans = factorial(m)//(factorial(m-n)*factorial(n))
    print(ans)