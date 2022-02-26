for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if m < n or n == 2:
        print(-1)
    else:
        print(sum(arr)*2)
        for k in range(1, n):
            print(k, k + 1)
        print(1, n)
