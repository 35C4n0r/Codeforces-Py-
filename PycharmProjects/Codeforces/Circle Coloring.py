for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    arr = []
    count = 0
    for (aa, bb, cc) in zip(a, b, c):
        if count != aa:
            arr.append(aa)
            count = aa
        elif count != bb:
            arr.append(bb)
            count = bb
        else:
            arr.append(cc)
            count = cc
    if arr[0] == arr[-1]:
        if a[-1] != arr[0] and a[-1] != arr[-2]:
            arr.insert(n, a[-1])
        elif b[-1] != arr[0] and b[-1] != arr[-2]:
            arr.insert(n, b[-1])
        else:
            arr.insert(n, c[-1])
        # print(lis)
        arr.pop(-2)
    print(*arr)
