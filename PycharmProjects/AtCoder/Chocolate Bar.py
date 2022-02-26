import itertools
import math
ans = math.inf
h, w = list(map(int, input().split()))
if (h*w) % 3 == 0:
    print(0)
else:
    for kk in range(1, w):
        a = h * kk
        b = (h//2) * (w - kk)
        c = (h*w) - (a+b)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        b = h * ((w-kk) // 2)
        c = (h * w) - (a + b)
        ans = min(ans, max(a, b, c) - min(a, b, c))
    for kk in range(1, h):
        a = w * kk
        b = (w//2) * (h - kk)
        c = (h*w) - (a+b)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        b = w * ((h-kk) // 2)
        c = (h*w) - (a+b)
        ans = min(ans, max(a, b, c) - min(a, b, c))
    print(ans)