# 900
for _ in range(int(input())):
    r, g, b = sorted(list(map(int, input().split())))
    if r + g + 1 >= b:
        print("Yes")
    else:
        print("No")
