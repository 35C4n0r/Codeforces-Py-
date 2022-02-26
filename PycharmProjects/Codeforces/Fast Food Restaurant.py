for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        print(0)
    elif a >= 4 and b >= 4 and c >= 4:
        print(7)
    else:
        pass