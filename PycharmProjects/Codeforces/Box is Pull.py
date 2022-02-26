for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if a == c and b == d:
        print(0)
    elif a == c:
        print(abs(b - d))
    elif b == d:
        print(abs(a - c))
    else:
        ans = abs(a - c) + abs(b - d) + 2
        print(ans)
