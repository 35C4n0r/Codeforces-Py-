n, k = list(map(int, input().split()))
arr = []
arr2 = []
count = 0
for _ in range(n):
    arr.append(int(input()))
    if n > 0:
        if abs(arr[_-1] - arr[_]) <= k:
            print(arr[_], arr[_-1])
            count += 1
print(count)
