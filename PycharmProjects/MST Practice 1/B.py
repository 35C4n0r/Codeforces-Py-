import math
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = {}
    arr2 = {}
    for k in range(m):
        a, b, c = list(map(int, input().split()))
        z = min(a, b)
        zz = max(a, b)
        if (z, zz) in arr:
            arr[z, zz].append(c)
        else:
            arr[z, zz] = [c]
        if a in arr2:
            arr2[a].append(b)
        else:
            arr2[a] = [b]
        if b in arr2:
            arr2[b].append(a)
        else:
            arr2[b] = [a]
    print(arr2)
    print(arr)
    xx = 1
    arr3 = [1]
    cost = 1
    while len(arr3) != n:
        arr4 = []
        arr100 = []
        for zzz in arr2[xx]:
            print(zzz)
            if zzz not in arr3:
                arr4.append(arr[min(xx, zzz), max(xx, zzz)])
                arr100.append(zzz)
        ym = min(arr4)
        print(ym)
        xx = arr100[arr4.index(ym)]
        for ymm in ym:
            cost *= ymm
        arr3.append(xx)
    print(int(math.log(cost, 2) + 1))
