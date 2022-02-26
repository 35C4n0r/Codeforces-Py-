for _ in range(int(input())):
    h, p = list(map(int, input().split()))
    while h > 0 and p > 0:
        h -= p
        p //= 2
    if p == 0 and h != 0:
        print(0)
    else:
        print(1)

