# 900
n = int(input())
arr = list(map(int, input().split()))
arr4 = arr.copy()
arr2 = sorted(arr, reverse=True)
arr3 = []
count = 0
result = 0
for k in arr2:
    z = arr.index(k)
    arr3.append(z + 1)
    arr.remove(k)
    arr.insert(z, "@")
    result += (k * count) + 1
    count += 1
print(result)
for kk in arr3:
    print(kk, end=" ")
