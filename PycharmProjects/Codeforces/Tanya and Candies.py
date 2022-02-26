n = int(input())
arr = list(map(int, input().split()))
count = 0
for k in range(n):
    se = 0
    so = 0
    arr2 = arr.copy()
    arr2.pop(k)
    for kk in range(0, n - 1, 2):
        se += arr2[kk]
    so = sum(arr2) - se
    if se == so:
        count += 1
print(count)