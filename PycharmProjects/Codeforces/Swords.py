import math
n = int(input())
arr = list(map(int, input().split()))
arr2 = list(set(arr))
arr3 = 0
arr2.sort()
z = arr2[0]
if z == 0:
    z = arr2[1]
zz = arr2[-1]
arr2.remove(zz)
g = zz - z
for k in arr2:
    g = math.gcd((zz - k), g)
for kk in arr:
    arr3 += (zz - kk) // g
print(arr3, g)


