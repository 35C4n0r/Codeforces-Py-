for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if a != c:
        print(a, c)
    elif b != d:
        print(b, d)
    elif a != d:
        print(a, d)
    elif b != c:
        print(b, c)
    else:
        print(a, b)