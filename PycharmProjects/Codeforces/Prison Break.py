for _ in range(int(input())):
    n, m, r, c = list(map(int, input().split()))
    print(max(r-1, n-r) + max(c-1, m-c))
