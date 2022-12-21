import sys
input = sys.stdin.readline

n, k = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0
result = -1

def merge_sort(A, p, r):
    if(p < r and cnt <= k):
        q = (p + r) // 2
        merge_sort(A, p , q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        
def merge(A, p, q, r):
    global cnt, result
    i = p
    j = q + 1
    temp = []
    # 둘 다 남은 경우
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    # 왼쪽 배열 부분이 남은 경우    
    while i <= q:
        temp.append(A[i])
        i += 1
    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        temp.append(A[j])
        j += 1
    
    i = p
    t = 0
    # 결과를 A[p..r]에 저장
    while i <= r:
        A[i] = temp[t]
        cnt += 1
        if cnt == k:
            result = A[i]
            break
        i += 1
        t += 1

merge_sort(data, 0, n - 1)
print(result)