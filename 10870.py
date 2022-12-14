import sys
input = sys.stdin.readline

n = int(input())
data = [0]*21
data[1] = 1

for i in range(2,21):
  data[i] = data[i-2]+data[i-1]

print(data[n])