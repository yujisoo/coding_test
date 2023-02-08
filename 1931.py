n = int(input())
meeting = [[0,0] for _ in range(n)]
for i in range(n):
    start,end = map(int,input().split())
    meeting[i] = [start,end]
meeting = sorted(meeting, key=lambda x: (x[1],x[0]))

end = meeting[0][1]
cnt = 1
for i in range(1,n):
    if meeting[i][0]>=end:
        cnt+=1
        end = meeting[i][1]
print(cnt)