import math
n, k = list(map(int, input().split()))
ans = math.inf
count = 0
arr = list(map(int, input().split()))
if len(set(arr)) == 1:
    print(1)
else:
    for kk in range(n - k + 1):
        arr2 = arr[kk:kk+k]
        xxx = sum(arr2)
        if xxx < ans:
            count = kk
            ans = xxx
    print(count + 1)