from itertools import permutations

n = int(input())
k = int(input())
card  = []
for _ in range(n):
    card.append(int(input()))
ans = list(permutations(card,k))
answer = []
for c in ans:
    num = ""
    for j in c:
        
        num += str(j)
    
    if num not in answer:
        answer.append(num)
print(len(answer))