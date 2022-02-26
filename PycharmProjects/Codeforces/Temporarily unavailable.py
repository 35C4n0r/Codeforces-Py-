# 900
for _ in range(int(input())):
    a, b, c, r = list(map(int, input().split()))
    a = min(a, b)
    b = max(a, b)
    if c < a or c > b:
        if r == 0:
            print(0)
        else:
            if c < a:
                count = ((b - a) - ((c + r) - a))
            else:
                count = ((b - a) - ((c - r) - a))
            print(count)
