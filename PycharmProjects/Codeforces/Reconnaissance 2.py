import math
ans = math.inf
ind1 = 0
ind2 = 0
n = int(input())
arr = list(map(int, input().split()))
for k in range(n - 1):
    z = abs(arr[k] - arr[k+1])
    if z < ans:
        ans = z
        ind1 = k
        ind2 = k+1
if abs(arr[0] - arr[-1]) < ans:
    print(1, n)
else:
    print(ind1 + 1, ind2 + 1)
