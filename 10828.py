import sys
input = sys.stdin.readline()
stack = []
for _ in range(int(input())):
    a = list(map(str,input().split()))
    if len(a)==2:
        stack.append(int(a[1]))
    else:
        if a[0]=="pop":
            if len(stack)==0:
                print(-1)
            else:
                b = stack.pop(-1)
                print(b)
        elif a[0]=="size":
            print(len(stack))
        elif a[0]=="top":
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])
        elif a[0]=="empty":
            if len(stack)==0:
                print(1)
            else:
                print(0)
        