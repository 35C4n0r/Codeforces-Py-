from sys import *
input = stdin.readline
for _ in range(int(input())):
    n, x, t = list(map(int, input().split()))
    z = t // x
    if z > n:
        print(n*(n-1) // 2)
    else:
        print(((n-z)*z) + (z*(z-1) // 2))