import sys
input = sys.stdin.readline

x,y,w,h = map(int,input().split())

a = w-x
b = h-y

print(min(a,b,x,y))