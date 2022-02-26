n = int(input())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []
j = 0
k = 0
for j in range(n):
    arr1.append(arr[j])
    for k in range(j + 1, n):
        if arr[k] not in arr1:
            arr1.append(arr[j])
        else:
            arr2.append(len(arr1))
            arr1 = []
        if j == n:
            arr2.append(len(arr1))
print(arr2)
