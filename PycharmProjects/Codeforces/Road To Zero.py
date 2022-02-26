for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    if 2*a <= b:
        print((x+y)*a)
    else:
        print((min(x, y) * b) + ((abs(x - y)) * a))

