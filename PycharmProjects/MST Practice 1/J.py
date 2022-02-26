for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = {}
    arr2 = {}
    visited = [1]
    cost = 0
    for j in range(k):
        a, b, c = list(map(int, input().split()))
        z = min(a, b)
        zz = max(a, b)
        if (z, zz) in arr2:
            arr2[z, zz].append(c)
        else:
            arr2[z, zz] = [c]
        if a in arr:
            arr[a].append(b)
        else:
            arr[a] = [b]
        if b in arr:
            arr[b].append(a)
        else:
            arr[b] = [a]
    print(arr)
    print(arr2)
    for c in range(1, n+1):
        z1 = []
        z2 = []
        for jj in arr[c]:
            if jj not in visited:
                print(jj)
                z1.append(arr2[min(jj, c), max(jj, c)])
                z2.append(jj)
        print(z1)

        if len(z1) > 0:
            abc = min(z1)
            print(abc, visited)
            abb = z2[z1.index(abc)]
            for abd in abc:
                visited.append(abb)
                cost += abd
    print(cost)


