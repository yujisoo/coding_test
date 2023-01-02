for _ in range(int(input())):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    cnt = 0
    
    for i in range(n):
        cx, cy, r = list(map(int,input().split()))

        # 출발점이 행성안에 있는지 확인
        dis1 = ((cx-x1)**2+(cy-y1)**2)**0.5
        # 도착점이 행성안에 있는지 확인
        dis2 = ((cx-x2)**2+(cy-y2)**2)**0.5
        if dis1 < r and dis2 < r:
            continue
        elif dis1 < r:
            cnt+=1
        elif dis2 < r:
            cnt+=1
        
    print(cnt)