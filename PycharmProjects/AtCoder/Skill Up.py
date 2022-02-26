n, m, x = list(map(int, input().split()))
arr3 = []
for _ in range(n):
    arr = list(map(int, input().split()))
    c = arr[0]
    arr2 = arr[1:]
    arr3.append(arr)
arr3.sort()
print(arr3)
