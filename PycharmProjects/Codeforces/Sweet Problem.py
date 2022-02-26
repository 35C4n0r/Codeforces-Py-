# 1100
for _ in range(int(input())):
    r, g, b = sorted(list(map(int, input().split())))
    if r == g == b:
        print(r)
    else:
        zz = r + min(g, b-r)
        print(zz)