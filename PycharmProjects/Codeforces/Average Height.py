for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ae = []
    ao = []
    e = 0
    o = 0
    for k in arr:
        if k % 2 == 0:
            ae.append(str(k))
        else:
            ao.append(k)
    print(*ae, *ao)
