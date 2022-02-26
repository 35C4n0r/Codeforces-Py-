for _ in range(int(input())):
    x, y, z = sorted(list(map(int, input().split())))
    if max(x, x) == x and max(x, z) == y and max(x, z) == z:
        print("YES")
        print(x, x, z)

    else:
        print("NO")