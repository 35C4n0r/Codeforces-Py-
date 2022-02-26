import math
for _ in range(int(input())):
    n, m, x = list(map(int, input().split()))
    a = math.ceil(x / n)
    b = 11 % 3
    print(b)