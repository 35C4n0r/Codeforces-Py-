for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    current = 1
    for s in arr:
        if s * current >= x:
            ans += 1
            current = 0
        current += 1
    print(ans)

