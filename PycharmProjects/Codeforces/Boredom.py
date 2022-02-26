arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
arr2 = arr.copy()
arr2.sort(key=lambda arr2: arr2[1])
arr.sort()
print(arr2)
print(arr)
if arr == arr2:
    print(arr2[-1][-1])
else:
    print(arr[-1][0])