import math
s, p = list(map(int, input().split()))
if s**2 >= 4*p:
    m = (s + math.sqrt((s**2) - (4*p))) / 2
    print(s + math.sqrt((s**2) - (4*p)))
    print(m, math.sqrt(999999999999999999999996), s**2-4)
    print(math.sqrt(5))
    if m == int(m):
        print('Yes')
else:
    print("No")