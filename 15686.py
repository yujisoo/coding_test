from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
city = []
home = []
chicken = []

for _ in range(n):
    city.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            home.append([i,j])
        elif city[i][j]==2:
            chicken.append([i,j])
ch = list(combinations(chicken,m))
answer = [0]*len(ch)

for i in range(len(ch)):
    for k in home:
        d = 1000000
        for j in range(len(ch[i])):
            d = min(d,abs(ch[i][j][0]-k[0])+abs(ch[i][j][1]-k[1]))
        answer[i]+=d
print(min(answer))