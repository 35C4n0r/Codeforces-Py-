n, k = list(map(int, input().split()))
if n < 2*k + 1:
    print(-1)
else:
    print(n*k)
    for kk in range(1, n+1):
        for kkk in range(1, k + 1):
            if kk + kkk > n:
                print(kk, (kk+kkk)%n)
            else:
                print(kk, kk+kkk)
            #print(kk, (kk+kkk)%jkj)