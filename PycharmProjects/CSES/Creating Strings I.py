import math
arr = list(input())
arr.sort()
result = []
import itertools
print()
for k in itertools.permutations(arr, len(arr)):
    result.append("".join(k))
z = set(result)
m = list(z)
m.sort()
print(len(m))
for f in m:
    print(f)


