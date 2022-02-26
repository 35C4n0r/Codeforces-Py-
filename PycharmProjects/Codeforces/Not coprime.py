import math
import itertools
from sys import *
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2 = []
pme = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for k in range(1, 16):
    dj = 1
    bless = False
    ins = list(itertools.combinations(pme, k))
    print(ins)
    for kk in ins:
        print(kk)
        dj *= kk
    for jj in arr:
        if math.gcd(dj, jj) > 1:
            bless = True
    if not bless:
        print(dj)
        break

'''ans = 1
flag = []
for k in lis:
    if k in pme and k not in flag:
        flag.append(k)
        ans *= k
    elif k % 2 == 0:
        if 2 not in flag and k // 2 not in flag:
            flag.append(2)
            ans *= 2
    else:
        for kk in range(2, 51):
            if k % kk == 0:
                if kk not in flag and k // kk not in flag:
                    flag.append(kk)
                    ans *= kk
                    break
                else:
                    break
    print(flag, k)
print(ans)'''