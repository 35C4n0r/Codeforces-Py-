import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = {}
    for k in range(n - 1):
        z = math.gcd(arr[k], arr[k+1])
        if z in arr:
            arr2[z].append(arr[k])
        if arr[k+1] not in arr
        else:
            arr2[z] = [arr[k]]
