n, m = list(map(int, input().split()))
if m == 0:
    for nnnn in range(1, n+1, 3):
        print(nnnn, nnnn+1, nnnn+2)
else:
    vis = [False]*n
    vec = []
    #print(vec)
    arr = [k for k in range(1, n+1)]

    arr2 = {}
    for _ in range(m):
        a, b = list(map(int, input().split()))
        if a in arr2:
            arr2[a].append(b)
        else:
            arr2[a] = [b]
        if b in arr2:
            arr2[b].append(a)
        else:
            arr2[b] = [a]
        if a in arr:
            arr.remove(a)
        if b in arr:
            arr.remove(b)
    #print(lis, arr2)
    flag = 0
    curr = 0
    ex = 0
    for kkkkk in arr2:
        if len(arr2[kkkkk]) > 2:
            print(-1)
            exit()
    while ex < n//3:
        ddg = []
        ex += 1
        for kkk in arr2:
            #print(kkk)
            for fuc in arr2[kkk]:
                ddg.append(fuc)
            ddg.append(kkk)
            #print(vec)
            if len(ddg) > 3:
                print(-1)
                exit()
            elif len(ddg) == 2 and len(arr) != 0:
                ddg.append(arr[0])
                arr.pop(0)
            elif len(ddg) == 2 and len(arr) == 0:
                print(-1)
                exit()
            for jj in ddg:
                if jj in arr2:
                    arr2.pop(jj)
            flag += 1
            vec.append(ddg)
            break
        #print(vec)
    for km in vec:
        print(*km)
    if len(arr) > 0:
        if len(arr)%3 == 0:
            for nmnm in range(0, len(arr), 3):
                print(arr[nmnm], arr[nmnm + 1], arr[nmnm+2])
        else:
            print(-1)
            exit()
