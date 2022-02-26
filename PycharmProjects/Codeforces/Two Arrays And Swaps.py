for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    brr = list(map(int, input().split()))
    brr.sort(reverse=True)
    count = 0
    for j in range(k):
        if arr[j] < brr[j]:
            arr[j] = brr[j]
    print(sum(arr))