import math
from sys import *
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
'''arr2 = lis.copy()
arr2.sort()
lis.insert(0, 0)
lis.append(math.inf)
for j in arr2:
    gg = lis.index(j)
    arr3 = lis[:gg]
    arr4 = lis[gg+1:]
    for kk in range(len(arr3)):
        if arr3[kk] > j and (arr3[kk]+j) % 2 != 0:
            lis[kk], lis[gg] = lis[gg], lis[kk]
            gg = kk
            break
    arr3 = lis[:gg]
    arr4 = lis[gg + 1:]
    for uu in range(len(arr4)):
        if arr4[uu] < j and (arr4[uu]+j) % 2 != 0:
            lis[gg+uu+1], lis[gg] = lis[gg], lis[gg+uu+1]
            break
    #print(lis, arr3, arr4, j)
lis.pop(0)
lis.pop(-1)
print(*lis)'''
odd = 0
even = 0
for kk in arr:
    if kk%2 == 0:
        even += 1
    else:
        odd += 1
    if even > 0 and odd > 0:
        arr.sort()
        print(*arr)
        exit()
print(*arr)