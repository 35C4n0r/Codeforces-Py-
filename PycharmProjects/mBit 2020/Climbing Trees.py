from sys import *
input = stdin.readline
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
pre = 0
flag = 0
best = 0
for a in arr:
    if a - flag <= k:
        pre += a
        flag = a
    else:
        flag = a
        pre = a
    best = max(best, pre)
    #print(a, best, pre, flag)
print(best)