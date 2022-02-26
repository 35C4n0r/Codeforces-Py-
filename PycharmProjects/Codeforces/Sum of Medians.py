for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    if n == 2 or n == 1:
        for kk in range(0, len(arr), n):
            ans += arr[kk]
    else:
        if (n-1) % 2 == 0:
            for kk in range(k+((n-1)//2) - 1, len(arr), (n-1)//2 + (n-1)//2):
                #print(kk)
                #print(kk)
                ans += arr[kk]
        else:
            for kk in range(k + ((n-1)//2) - 1, len(arr), n - 1):
                # print(kk)
                # print(kk)
                ans += arr[kk]
    print(ans)