n = int(input())
m = list(map(int,input().split()))
city = list(map(int,input().split()))
total = 0
a = 0
for i in range(n-1):
    if i == 0:
        a = city[0]
        total += m[0]*a
    else:
        if city[i]<a:
            a = city[i]
            total+=a*m[i]
        else:
            total+=a*m[i]

print(total)