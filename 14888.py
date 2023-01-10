n = int(input())
a = list(map(int,input().split()))
m = list(map(int,input().split()))

maximun = -1000000000
minimun = 100000000

def dfs(depth, ans, plus, minus, multi, div):
    global maximun, minimun
    if depth == n:
        maximun = max(maximun, ans)
        minimun = min(minimun, ans)
        return

    if plus > 0:
        dfs(depth+1, ans+a[depth], plus-1, minus, multi, div)
    if minus > 0:
        dfs(depth+1, ans-a[depth], plus, minus-1, multi, div)
    if multi > 0:
        dfs(depth+1, ans*a[depth], plus, minus, multi-1, div)
    if div > 0:
        dfs(depth+1, int(ans/a[depth]), plus, minus, multi, div-1)

dfs(1,a[0],m[0],m[1],m[2],m[3])
print(maximun)
print(minimun)