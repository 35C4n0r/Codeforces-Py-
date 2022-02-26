from sys import *
input = stdin.readline
import math
from collections import Counter
s = input()
n = len(s)
arr = Counter(list(s.strip()))
print(arr)
ans = []
#zm = 0
ss = max(arr.values())
cc = ss
#xx = math.gcd()
for k in arr:
    cc = math.gcd(arr[k], cc)
    print(cc, k, ss)
    if cc == 1:
        print("IMPOSSIBLE")
        exit()
    else:
        ans.append(k*(arr[k]//cc))
print(''.join(ans))