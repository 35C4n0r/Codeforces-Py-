import math
n = int(input())
arr = list(map(int, input().split()))
curr = 0
true_ans = arr[0]
ans = 0
arr.sort()
for k in range(2, 1001):
    for kk in range(n):
        if arr[kk] % k == 0:
            curr += 1
    if curr >= ans:
        ans = curr
        true_ans = k
    curr = 0
print(true_ans)