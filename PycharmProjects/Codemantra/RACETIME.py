import math
time = 0
u = 0
dist = []
for _ in range(int(input())):
    a, b, g = list(map(int, input().split()))
    l, q = list(map(int, input().split()))
    for i in range(q):
        p, d = list(map(int, input().split()))
        dist.append(d)
        if p != 1 and p != 3 :
            time = -u + math.sqrt((u ** 2) + (2 * a * p))
            v = a * time
        elif p == 1:
            time += -v + math.sqrt((v ** 2) - (2 * b * ))
            u =
