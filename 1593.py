a,b = map(int,input().split())
w = input()
s = input()
cnt = 0

wa = [0] * 58
sa = [0] * 58
for i in w:
    wa[ord(i) - 65] += 1
    
start = 0
length = 0
for i in range(b):
    sa[ord(s[i])-65]+=1
    length += 1
    if length == a:
        if wa == sa:
            cnt+=1
        sa[ord(s[start])-65]-=1
        start += 1
        length -= 1
print(cnt)