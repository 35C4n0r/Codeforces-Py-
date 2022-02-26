import math
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    count = 0
    if a == b:
        print(0)
    elif b % a == 0:
        z = b // a
        if z % 2 == 0:
            zz = int(math.sqrt(z))
            count += zz // 3
            zz = zz % 3
            count += zz // 2
            zz = zz % 2
            count += zz // 1
            print(count)
        else:
            print(-1)
    elif a % b == 0:
        z = a // b
        if z % 2 == 0:
            zz = int(math.sqrt(z))
            count += zz // 3
            zz = zz % 3
            count += zz // 2
            zz = zz % 2
            count += zz // 1
            print(count)
        else:
            print(-1)
    else:
        print(-1)
