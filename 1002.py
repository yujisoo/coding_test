for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    # 동심원
    if d == 0 and r1 == r2:
        print(-1)
    # 내접 외접
    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    # 두점에서 만날 때
    elif abs(r1-r2) < d < (r1+r2) :
        print(2)
    else:
        print(0) 