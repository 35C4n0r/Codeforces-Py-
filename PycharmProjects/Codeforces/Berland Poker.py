for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    each = n // k
    if m == 0:
        print(0)
    else:
        d = n // k
        a1 = min(m, d)
        a2 = (m - a1 + k - 2) // (k - 1)
        print(a1 - a2)