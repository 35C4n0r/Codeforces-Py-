for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, list(str(n))))
    for j in range(k-1):
        n += min(arr)*max(arr)
        arr = list(map(int, list(str(n))))
        if 0 in arr:
            break
    print(n)