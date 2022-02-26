for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr)
    arr.insert(0, 1)
    count = 1
    mis = 0
    z = n - len(set(arr))
    if n >= max(arr):
        print(n + 1)
    else:
        for k in range(n - 1):
            zz = arr[k+1]-arr[k]
            if zz > 1:


