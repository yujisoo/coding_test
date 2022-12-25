import sys
input = sys.stdin.readline

n = int(input())

def star(n) :
    if n==1:
        return ["*"]
    a = star(n//3)
    l = []
    
    for i in a:
        l.append(i*3)
    for i in a:
        l.append(i+" "*(n//3)+i)
    for i in a:
        l.append(i*3)
    return l
    
print("\n".join(star(n)))