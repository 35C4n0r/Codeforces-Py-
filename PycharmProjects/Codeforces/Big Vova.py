import itertools
import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = arr[0]
    for k in range(1, n):
        for kk in range(k + 1, n):
            if math.gcd(arr[k], ans) < math.gcd(arr[kk], ans):
                (arr[k], arr[kk]) = (arr[kk], arr[k])
            #print(lis)
        ans = math.gcd(ans, arr[k])
    print(*arr)

