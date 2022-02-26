#THIS CODE IS PROPERTY OF NO_SOUL
for _ in range(int(input())):
    n = int(input())
    arr = [kk for kk in range(1, n+1)]
    arr.sort(reverse=True)
    if n%2 != 0:
        arr[(n-1) // 2], arr[0] = arr[0], arr[(n-1) // 2]
    print(*arr)