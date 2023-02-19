import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
start = 1
check = True

for _ in range(n):
    k = int(input())
    while start<=k:
        a.append(start)
        b.append("+")
        start+=1
    if a[-1] == k:
        a.pop()
        b.append("-")
    else:
        print("NO")
        check = False
        break

if check==True:
    for i in b:
        print(i)