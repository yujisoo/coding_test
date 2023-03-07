import sys
input = sys.stdin.readline

n,c = map(int,input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
start = 1
end = house[-1]-house[0]
ans = 0
while True:
    if start >end:
        break
    mid = (start+end)//2
    now = house[0]
    cnt = 1

    for i in range(1,n):
        if house[i]>=now+mid:
            cnt+=1
            now = house[i]
    if cnt >=c :
        start = mid+1
        ans = mid
    else:
        end = mid-1
print(ans)