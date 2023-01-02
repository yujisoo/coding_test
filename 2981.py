import sys
input = sys.stdin.readline
import math

n = int(input())
num = []
m = []
a = []
for _ in range(n):
    num.append(int(input()))
num.sort()

for i in range(1,len(num)):
    a.append(num[i]-num[i-1])

first = a[0]
for i in range(1,len(a)):
    first = math.gcd(first,a[i])

for i in range(2,int(first**0.5)+1):
    if first % i == 0:
        m.append(i)
        m.append(first//i)

m.append(first)
m.sort()
m = set(m)
        
print(*m)