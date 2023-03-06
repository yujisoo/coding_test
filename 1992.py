n = int(input())
record = []

for _ in range(n):
    record.append(list(map(int,input())))
def find(start_r,start_c,n):
    if n == 1:
        print(record[start_r][start_c],end="")
        return 0
    num = record[start_r][start_c]

    for i in range(start_r,start_r+n):
        for j in range(start_c,start_c+n):
            if num != record[i][j]:
                print("(",end="")
                n //= 2
                find(start_r,start_c,n)
                find(start_r,start_c+n,n)
                find(start_r+n,start_c,n)
                find(start_r+n,start_c+n,n)
                print(")",end="")
                return 0
    print(record[start_r][start_c],end="")
    return 0
find(0,0,n)