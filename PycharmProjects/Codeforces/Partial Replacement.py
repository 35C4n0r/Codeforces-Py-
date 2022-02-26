for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    ar = input()
    lis = list(ar)
    #print(lis)
    z = ar.index('*') + 1
    lis.reverse()
    zz = len(ar) - lis.index('*')

    #print(gg, zz)
    ans = zz - z
    ans //= k
    if zz == z:
        print(1)
    else:
        print(ans + 2)
