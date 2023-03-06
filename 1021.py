from collections import deque

n,m = map(int,input().split())
ans = list(map(int,input().split()))
num = deque()
for i in range(1,n+1):
    num.append(i)
cnt = 0
for i in ans:
    n = num.index(i)
    if n<len(num)//2+1:
        while True:
            if num[0]==i:
                num.popleft()
                break
            else:
                a = num.popleft()
                cnt+=1
                num.append(a)
    else:
        while True:
            if num[0]==i:
                num.popleft()
                break
            else:
                a = num.pop()
                cnt+=1
                num.appendleft(a)
print(cnt)