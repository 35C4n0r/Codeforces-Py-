import itertools
sum = 0
n = int(input())
arr = list(map(int, input().split()))
arr2 = arr.copy()
arr2.sort(reverse=True)
arr = list(set(arr))
arr.sort(reverse=True)
for k in itertools.combinations(arr, 2):
    z = arr2.count(k[0])
    zz = arr2.count(k[1])
    pure = z*zz
    sum += (k[0] - k[1]) * pure
print(sum)