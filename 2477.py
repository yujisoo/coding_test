k = int(input())

data = []
for _ in range(6):
    a, b = map(int,input().split())
    data.append([a,b])

w = 0
h = 0
max_w = 0
max_h = 0

for i in range(6):
    if data[i][0] == 1 or  data[i][0] == 2:
        if max_w < data[i][1]:
            max_w = data[i][1]
            w = i 
    else:
        if max_h < data[i][1]:
            max_h = data[i][1]
            h = i

minus_w = abs(data[(h-1)%6][1]-data[(h+1)%6][1])
minus_h = abs(data[(w-1)%6][1]-data[(w+1)%6][1])
ans = (max_w * max_h - minus_w * minus_h)*k
print(ans)