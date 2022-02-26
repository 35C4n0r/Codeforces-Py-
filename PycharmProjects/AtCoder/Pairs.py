import itertools
n, kk = list(map(int, input().split()))
arr = list(map(int, input().split()))
# arr.sort(reverse=True)
arr2 = []
print(arr)
for k in itertools.combinations(arr, 2):
    arr2.append(k[0]*k[1])
arr2.sort()
print(arr2[kk - 1])
