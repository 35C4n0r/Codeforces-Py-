for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    count = 0
    for j in arr[1:]:
        if j <= k:
            count += (k-j) // arr[0]
    print(count)
