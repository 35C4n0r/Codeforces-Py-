for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    z = 2 * min(a, b)
    if z >= max(a, b):
        print(z**2)
    else:
        print(max(a, b)**2)