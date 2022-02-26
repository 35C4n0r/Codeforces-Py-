for _ in range(int(input())):
    p, q = list(map(int, input().split()))
    if p < q:
        print(p)
    elif p >= q:
        for k in range(min(p//2, q - 1), 0, -1):
            if p % k == 0:
                print(k)
                break