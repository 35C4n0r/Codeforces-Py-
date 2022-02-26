import math
k, m, n = list(map(int, input().split()))
t = 10*k
if n >= t:
    print(0)
else:
    es = t - n
    print(math.ceil(es / m))