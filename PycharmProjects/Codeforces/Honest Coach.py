for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 10**9
    if len(set(arr)) != len(arr):
        print(0)
    else:
        for i in range(len(arr) - 1):
            count = min(count, arr[i+1]-arr[i])
        print(count)
