import math

n = int(input())
ans = list(map(int,str(math.factorial(n))))
ans.reverse()
cnt = 0
for i in ans:
    if i == 0:
        cnt+=1
    else:
        break
print(cnt)