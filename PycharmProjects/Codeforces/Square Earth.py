n, x1, y1, x2, y2 = list(map(int, input().split()))
peri = 4 * n
if x1 == x2 or y1 == y2:
    dist = abs(y1 - y2) + abs(x1 - x2)
elif x1 == 0 and x2 == n or x2 == 0 and x1 == n:
    dist = n + abs(y1) + abs(y2)
elif y1 == 0 and y2 == n or y2 == 0 and y1 == n:
    dist = n + x1 + x2
elif x1 == 0 and n > x2 > 0 == y2:
    dist = abs(y1 - n) + y2
elif x2 == 0 and n > x1 > 0 == y1:
    dist = abs(y2 - n) + y1
print(min(dist, peri - dist))


