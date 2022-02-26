for _ in range(int(input())):
    arr = []
    n, m = list(map(int, input().split()))
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    lmao = False
    for k in range(n):
        for kk in range(m):
            smh = 4
            if k == 0 or k == n-1:
                smh -= 1
            if kk == 0 or kk == m-1:
                smh -= 1
            if arr[k][kk] > smh:
                lmao = True
                break
            arr[k][kk] = smh
    if lmao == True:
        print("NO")
    else:
        print("YES")
        for cuteatime in arr:
            print(*cuteatime)
