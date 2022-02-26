for _ in range(int(input())):
    z = []
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for a in arr:
        if k % a == 0:
            z.append(k // a)
        else:
            z.append(0)
        q = z.copy()
    if sum(z) == 0:
        print(-1)
    else:
        while 0 in z:
            z.remove(0)
        b = min(z)
        c = q.index(b)
        d = arr[c]
        print(d)





