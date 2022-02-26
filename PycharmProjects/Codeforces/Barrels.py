for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    count = arr[0]
    #print(lis)
    for km in range(min(k, len(arr) - 1)):
        count += arr[km + 1]
    print(count)

