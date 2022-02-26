arr2 = []
arr5 = []
arr4 = []
arr6 = []
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))
    arr5.append(min(arr) / 2)
    if arr not in arr2:
        arr2.append(arr)
arr2.sort()
import itertools
for k in itertools.combinations(arr2, 2):
    arr3 = list(set(k[0]).intersection(k[1]))
    if len(arr3) == 2:
        q = arr3[0]
        w = arr3[1]
        zz = min(q, w, (sum(k[0])-(q+w) + sum(k[1])-(q+w)))
        zz /= 2
        arr4.append(zz)
ii = max(arr5)
iii = max(arr4)
iiii = max(ii, iii)
if ii in arr5:
    ss = arr5.index(int(iiii * 2))
    xxx = 1
else:
    ss = arr4.index(int(iiii * 2))
    xxx = 2
print(xxx)
print(iiii)