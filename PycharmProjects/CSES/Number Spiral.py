for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x % 2 == 0 and y <= x:
        print((x ** 2) - (y - 1))
    elif x % 2 != 0 and y <= x:
        print((x ** 2) - (y - 1))
    elif x % 2 != 0 and y > x:
        print((y ** 2) - x)
    elif x % 2 == 0 and y > x:
        print()


