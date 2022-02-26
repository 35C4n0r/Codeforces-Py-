import math
n, t = list(map(int, input().split()))
time = math.inf
arr2 = []
index = 0
ind = 0
for _ in range(n):
    ind += 1
    s, d = list(map(int, input().split()))
    if s >= t:
        if time > s:
            time = s
            index = ind
    else:
        z = math.ceil((t-s) / d)
        s += z * d
        if time > s:
            time = s
            index = ind
print(index)