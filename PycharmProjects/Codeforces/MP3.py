'''from sys import *
import math
input = stdin.readline
n, i = list(map(int, input().split()))
arr = list(map(int, input().split()))
space = 8*i
if n*(math.log2(len(set(arr)))) <= space:
    print(0)
else:
    #lis.sort()
    req = int(2 ** (space / n))
    arr3 = {}
    for _ in arr:
        if _ not in arr3:
            arr3[_] = 0
        arr3[_] += 1
    print(arr3)
    print(req)'''
n = int(input())
import math
import itertools
arr = list(map(int, input().split()))
ans = 0
for k in itertools.combinations(arr, 2):
    ans += math.gcd(k[0], k[1])
    print(k)
print(ans)