arr = {}
n, m = list(map(int, input().split()))
vis = [False]*n
for _ in range(m):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
    else:
        arr[a] = [b]
    if b in arr:
        arr[b].append(a)
    else:
        arr[b] = [a]
if 1 not in arr:
    print('IMPOSSIBLE')
else:
    arr3 = arr[1]
    for jj in arr3:
        if jj in arr:
            zz = arr[jj]
            if n in zz:
                print("POSSIBLE")
                exit()
print('IMPOSSIBLE')
