import sys
input = sys.stdin.readline

a = 1000000007
n = int(input())
num = [[1, 1], [1, 0]]

def mul(arr1,arr2):
    ans = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += arr1[i][k]*arr2[k][j]%a
    return ans

def div(n,num):
    if n == 1:
        return num
    elif n == 2:
        return mul(num,num)
    else:
        temp = div(n//2,num)
        if n%2==0:
            return mul(temp,temp)
        else:
            return mul(mul(temp,temp),num)

ans = div(n,num)
print(ans[1][0]%a)