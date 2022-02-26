# 900
for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    if b - a == 1 and c - b == 1 or b - a == 0 and c - b == 1 or b - a == 1 and c - b == 0 :
        print(0)
    elif b == a == c:
        print(0)
    else:
        a = a + 1
        c = c + 1
        print(abs(a - b) + abs(b - c) + abs(c - a))
