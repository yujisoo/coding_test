for _ in range(int(input())):
    n = int(input())
    wear = []
    cnt = []
    ans = 1
    for i in range(n):
        a,b = map(str,input().split())
        if b not in wear:
            wear.append(b)
            cnt.append(1)
        else:
            c = wear.index(b)
            cnt[c] += 1

    for i in cnt:
        ans *= (i+1)
    print(ans-1)

