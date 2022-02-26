from sys import *
input = stdin.readline
import math
n, m, k = list(map(int, input().split()))
if k == 0:
    print(-1)
    exit()
arr = {}
arr2 = {}
cost = math.inf
once = False
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
    else:
        arr[a] = [b]
    if b in arr:
        arr[b].append(a)
    else:
        arr[b] = [a]
    if (min(b, a), max(b, a)) in arr2:
        arr2[min(b, a), max(b, a)].append(c)
    else:
        arr2[min(b, a), max(b, a)] = [c]
arr3 = list(map(int, input().split()))
print(arr)
print(arr2)
for kk in arr3:
    if kk in arr:
        arr10 = set(arr[kk])
        #print(arr10)
        for kj in arr10:
            if kj not in arr3:
                arr5 = arr2[min(kk, kj), max(kk, kj)]
                for kkk in arr5:
                    once = True
                    cost = min(cost, kkk)
if not once:
    print(-1)
else:
    print(cost)