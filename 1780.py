n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))
cnt1 = 0
cnt0 = 0
cnt_m1 = 0
def div(start_r,start_c,size):
    global cnt0, cnt1, cnt_m1
    num = paper[start_r][start_c]
    for i in range(start_r,start_r+size):
        for j in range(start_c,start_c+size):
            if num != paper[i][j]:
                size = size//3
                for a in range(3):
                    for b in range(3):
                        div(start_r+a*size,start_c+b*size,size)
                return 0
    if num == 1:
        cnt1+=1
    elif num == 0:
        cnt0+=1        
    else:
        cnt_m1+=1
div(0,0,n)

print(cnt_m1)
print(cnt0)
print(cnt1)