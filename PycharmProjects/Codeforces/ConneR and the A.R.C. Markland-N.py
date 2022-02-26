import math
for _ in range(int(input())):
    n, s, k = list(map(int, input().split()))
    arr = sorted((list(map(int, input().split()))))
    ss = math.inf
    sss = math.inf
    for a in range(s, 0, -1):
        if a not in arr:
            ss = s - a
            break
    for aa in range(s, n+1):
        if aa not in arr:
            sss = aa - s
            break
    print(min(ss, sss))