import math
n = int(input())
arr = list(map(int, input().split()))
req = 0
if n == 1:
    print("YES")
else:
    for k in set(arr):
        req = max(req, arr.count(k))
    if n - req >= req - 1:
        print("YES")
    else:
        print("NO")

