#THIS PROPER OF NO_SOUL

from sys import *
import math
input = stdin.readline
for _ in range(int(input())):
    sna = math.inf
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1 and n > 1:
        print(-1)
    else:
        aaa = {}
        aaaa = {}
        for kk in range(n):
            if arr[kk] not in aaaa:
                aaaa[arr[kk]] = 1
            else:
                aaaa[arr[kk]] = 2
            aaa[arr[kk]] = kk + 1
        for kj in aaa:
            if aaaa[kj] == 1:
                if sna > kj:
                    inde = aaa[kj]
                    sna = kj
        if sna == math.inf:
            print(-1)
        else:
            print(inde)