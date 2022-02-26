import math
a, b = list(map(int, input().split()))
count = []
for _ in range(int(input())):
    x, y, v = list(map(int, input().split()))
    zz = math.sqrt(x**2 + y**2)
    zz = round(zz)
    count.append(zz/v)
print(round(min(count), 6))
