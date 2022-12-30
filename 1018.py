import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = []
cnt = 100000

for i in range(n):
    board.append(list(input().strip()))

# 8x8 체스판으로 자르기 위해 -7로 고정
for a in range(n-7):
    for b in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                # 합이 짝수/홀수 경우 각각 일정한 색을 가지게 됨
                if (i+j)%2==0:
                    if board[i][j] != 'W':
                        cnt1+=1
                    if board[i][j] != 'B':
                        cnt2+=1
                else:
                    if board[i][j] != 'B':
                        cnt1+=1
                    if board[i][j] != 'W':
                        cnt2+=1

        # 가장 작은 값으로 cnt 설정
        cnt = min(cnt1,cnt2,cnt)

print(cnt)