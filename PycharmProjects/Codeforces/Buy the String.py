from sys import *
input = stdin.read
for _ in range(int(input())):
    # THIS CODE IS PROPERTY OF NO_SOUL
    n, jh, smh, h = list(map(int, input().split()))
    s = input()
    abcd = list(map(int, list(s)))
    s = int(s)
    a1 = 0
    if 1 in abcd:
        a1 = abcd.count(1)
    b0 = n - a1
    print(min((b0 * jh + a1 * smh), (a1 * h + n * jh), (b0 * h + n * smh)))
