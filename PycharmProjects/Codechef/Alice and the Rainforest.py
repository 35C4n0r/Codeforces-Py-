import math
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    m = x+1
    mm = n - x
    leaf = math.ceil(math.log2(10))
    if m < leaf:
        ans1 = 2**x
    elif m == leaf:
        ans1 = (2**m) - n - (2**x)
