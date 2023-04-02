import sys,heapq
input = sys.stdin.readline

n = int(input())
left = []
right = []

for i in range(n):
    num = int(input())
    if len(left)==len(right):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)
    if len(right)>0 and right[0]<-left[0]:
        r = heapq.heappop(right)
        l = heapq.heappop(left)

        heapq.heappush(left,-r)
        heapq.heappush(right,-l)
    print(left)
    print(right)
    print(-left[0])