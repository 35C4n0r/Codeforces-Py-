import math
for _ in range(int(input())):
    n = int(input())
    count = 0
    if n == 1:
        count = 0
    else:
        z = int((-1 + math.sqrt(1+(24*n))) // 6)
        n -= (((3*z) + 1)*z)//2
        for k in range(z):
            z -= 1
            if n - (((3*z) + 1)*z)//2 >= 0:
                if n >= (((3 * z) + 1) * z)//2:
                    n -= (((3 * (z)) + 1) * (z)) // 2
                    count += 1
    print(count)
