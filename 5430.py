import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    p = list(map(str,input()))
    n = int(input())
    a = deque()
    a1= input().rstrip()
    if n > 0:
        for i in a1[1:len(a1)-1].split(","):
                a.append(i)
    idx = 0
    check = 0
    for i in p:
        if i == "R":
            if idx == 0:
                idx = -1
            else:
                idx = 0
        elif i == "D":
            if len(a)==0:
                print("error")
                check = 1
                break
            else:
                if idx == -1:
                    a.pop()
                else:
                    
                    a.popleft()
    if check==0:
        b = []
        if idx == -1:
            a.reverse()
        print("["+",".join(list(a))+"]")