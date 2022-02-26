n, m, k = list(map(int , input().split()))
arr = []
for _ in range(n):
    arr.append([0]*m)
#print(lis)
for _ in range(k):
    a, b, c = list(map(int, input().split()))
    if a == 1:
        for k in range(m):
            arr[b-1][k] = c

    else:
        for kk in arr:
            kk[b-1] = c
for _ in arr:
    print(*_)
