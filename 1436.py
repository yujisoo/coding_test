import sys
input = sys.stdin.readline

n = int(input())

a = 666
cnt = 0

while True:
    if '666' in str(a):
        cnt+=1
    if cnt==n:
        print(a)
        break    
    a+=1