# 1000
for _ in range(int(input())):
    z = int(input())
    count = 0
    b = 0
    for d in range(9):
        b = (b * 10) + 1
        for k in range(1, 10):
            if b * k <= z:
                count += 1
    print(count)

