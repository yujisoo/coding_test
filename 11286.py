import sys,heapq
input = sys.stdin.readline
heap1 = []
heap2 = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        if len(heap1) != 0 and len(heap2) != 0 :
            a = heapq.heappop(heap1)
            b = heapq.heappop(heap2)
            if a<b:
                print(a)
                heapq.heappush(heap2,b)
            else:
                print(-b)
                heapq.heappush(heap1,a)
        elif len(heap1) == 0 and len(heap2) != 0 :
            b = heapq.heappop(heap2)
            print(-b)
        elif len(heap1) != 0 and len(heap2) == 0 :
            a = heapq.heappop(heap1)
            print(a)
        else:
            print(0)
    elif x<0:
        heapq.heappush(heap2,-x)
    else:
        heapq.heappush(heap1,x)
