n = int(input())
data = list(map(int,input().split()))
data.sort()
if n%2!=0:
    a = n//2
    print(data[a]**2)
else:
    print(data[0]*data[-1])