a = []
for _ in range(4):
    a.append(list(map(int,input())))

k = int(input())
turn = []
for _ in range(k):
    a1,b1 = map(int,input().split())
    turn.append([a1,b1])

#시계 방향 회전
def clk(n):
    end = a[n].pop(-1)
    a[n].insert(0,end)
#반시계 방향 회전
def unclk(n):
    start = a[n].pop(0)
    a[n].append(start)
    

def midturn(ac,ar,al,af,r):
    data = [False]*4 
    data[ac] = True
    if a[ac][6] != a[al][2]:
        data[al] = True
    if a[ac][2] != a[ar][6]:
        data[ar] = True
    if af == 0 :
        if a[af][2] != a[al][6] and data[al]==True:
            data[af] = True
    else:
        if a[af][6] != a[ar][2] and data[ar]==True:
            data[af] = True
    #시계방향
    if r == 1:
        for i in range(4):               
            if data[i] == True:
                if i==ac or i==af:
                    clk(i)
                else:
                    unclk(i)
    #반시계방향
    else:
        for i in range(4):
            if data[i] == True:
                if i==ac or i==af:
                    unclk(i)
                else:
                    clk(i)

def firstturn(r):
    data = [False]*4
    data[0] = True
    if a[0][2] != a[1][6]:
        data[1] = True
    if a[1][2] != a[2][6] and data[1] == True:
        data[2] = True
    if a[2][2] != a[3][6] and data[2] == True:
        data[3] = True 
    #시계방향
    if r == 1:
        for i in range(4):
            if data[i]==True:
                if i == 0 or i == 2:
                    clk(i)
                else:                        
                    unclk(i)
            else:
                break
        #반시계방향
    else:
        for i in range(4):
            if data[i]==True:
                if i == 0 or i == 2:
                    unclk(i)
                else:
                    clk(i)
            else:
                break

def endturn(r):
    data = [False]*4
    data[3] = True
    if a[2][2] != a[3][6]:
        data[2] = True
    if a[1][2] != a[2][6] and data[2] == True:
        data[1] = True
    if a[0][2] != a[1][6] and data[1] == True:
        data[0] = True
    #시계방향
    if r == 1:            
        for i in range(4):
            if data[i]==True:
                if i == 1 or i == 3:
                    clk(i)
                else:
                    unclk(i)
    #반시계방향
    else:
        for i in range(4):
            if data[i]==True:
                if i == 1 or i == 3:
                    unclk(i)
                else:
                    clk(i)

for i in range(k):
    n = turn[i][0]
    r = turn[i][1]
    if n==1:
        firstturn(r)
    elif n==4:
        endturn(r)
    elif n==2:
        midturn(1, 2, 0, 3, r)
    else:
        midturn(2, 3, 1, 0, r)
        
ans = 0
if a[0][0] == 1:
    ans+=1
if a[1][0] == 1:
    ans+=2
if a[2][0] == 1:
    ans+=4
if a[3][0] == 1:
    ans+=8
print(ans)