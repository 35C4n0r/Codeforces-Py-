from sys import *
input = stdin.readline
n = int(input())
am = 0
bm = 0
cm = 0
dm = 0
em = 0
for _ in range(n):
    a, b, c, d, e = list(map(int, input().split()))
    am = max(a, am)
    bm = max(b, bm)
    cm = max(c, cm)
    dm = max(d, dm)
    em = max(e, em)
print(min(am, bm, cm, dm, em))