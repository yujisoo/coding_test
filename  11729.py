import sys
input = sys.stdin.readline

n = int(input())

def move(n,start,end):
    if n > 1 :
        move(n-1,start,6-start-end)
    print(start,end)
    if n > 1 :
        move(n-1,6-start-end,end)
    return
    
print(2**n-1)
move(n,1,3)