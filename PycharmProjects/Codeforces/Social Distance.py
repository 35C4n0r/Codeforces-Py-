for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, list(input())))
    print(arr)
    count = 0
    pre = 0
    z = arr.count(1)
    for x in range(n):
        if arr[x] == 1:
            if x - pre > k:
                count += 1
                pre = x
    print(count)



