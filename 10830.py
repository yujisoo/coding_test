import sys
input = sys.stdin.readline

n,b = map(int,input().split())
num = []

for _ in range(n):
    num.append(list(map(int,input().split())))

def sol(arr1,arr2):
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += (arr1[i][k]*arr2[k][j])
            ans[i][j]%=1000
    return ans
def cal(n,b,num):
    if b == 1:
        return num
    elif b == 2:
        return sol(num,num)
    else:
        temp = cal(n,b//2,num)
        if b%2 == 0:
            return sol(temp,temp)
        else:
            return sol(sol(temp,temp),num)
answer = cal(n,b,num)

for i in answer:
    for j in i:
        print(j%1000,end = ' ')
    print()