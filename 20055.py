n,k = map(int,input().split())
container = list(map(int,input().split()))
robot = [0]*(2*n)
cnt = 0

while True:
    cnt += 1
    #1단계
    c = container.pop(-1)
    container.insert(0,c)
    robot.pop(-1)
    robot.insert(0,0)
    if robot[n-1]!=0:
        robot[n-1]=0
    #2단계
    for i in range(n-2,0,-1):
        if robot[i]==1:
            if robot[i+1]==0 and container[i+1]>0:
                robot[i]=0
                robot[i+1]=1
                container[i+1]-=1
    if robot[n-1]!=0:
        robot[n-1]=0

    #3단계
    if container[0]>0 and robot[0]==0:
        robot[0]+=1
        container[0]-=1
    #4단계
    if container.count(0)>=k:
        print(cnt)
        break