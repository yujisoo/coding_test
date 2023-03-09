import sys
input = sys.stdin.readline

n,l = map(int,input().split())
m = []
for _ in range(n):
    m.append(list(map(int,input().split())))
ans = 0
#가로 길 확인
for i in range(n):
    now = m[i][0]
    cnt = 0
    check = 0
    slide = [0]*n
    for j in range(n):
        if now == m[i][j]:
            cnt += 1
            continue
        else:
            if now-m[i][j]==-1:
                if cnt>=l and sum(slide[j-l:j])==0:
                    cnt = 1
                    now = m[i][j]
                    continue
                else:
                    check = 1
                    break
            elif now-m[i][j]==1:
                now = m[i][j]
                cnt = 1
                if j+l <= n:
                    for k in range(j,j+l):
                        if now != m[i][k]:
                            check = 1
                            break
                        else:
                            slide[k] = 1
                else:
                    check = 1
                    break
            else:
                check=1
                break
    if check == 0:
        ans += 1
#세로 길 확인
for i in range(n):
    now = m[0][i]
    cnt = 0
    check = 0
    slide = [0]*n
    for j in range(n):
        if now == m[j][i]:
            cnt += 1
            continue
        else:
            if now-m[j][i]==-1:
                if cnt>=l and sum(slide[j-l:j])==0:
                    cnt = 1
                    now = m[j][i]
                    continue
                else:
                    check = 1
                    break
            elif now-m[j][i]==1:
                now = m[j][i]
                cnt = 1
                if j+l <= n:
                    for k in range(j,j+l):
                        slide[k] = 1
                        if now != m[k][i]:
                            check = 1
                            break
                            
                else:
                    check = 1
                    break
            else:
                check=1
                break
    if check == 0:
        ans += 1
print(ans)