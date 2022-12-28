import sys
input = sys.stdin.readline

n = int(input())
m = 0

for i in range(1, n+1):
    # 각 자리수를 합한 값을 구하기 위해 sum함수 사용
    a = i + sum(map(int,str(i)))
    if a == n:
        m = i
        break
    
print(m)