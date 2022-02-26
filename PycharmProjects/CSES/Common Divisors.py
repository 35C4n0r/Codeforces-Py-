import itertools
import math
a = int(input())
arr1 = []
arr = list(map(int, input().split()))
for i in itertools.combinations(arr, 2):
    k = math.gcd(i[0], i[1])
    arr1.append(k)
print(max(arr1))

