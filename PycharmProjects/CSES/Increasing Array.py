n = int(input())
arr = list(map(int, input().split()))
count = 0
i = 0
for _ in range(len(arr) - 1):
    while arr[i] > arr[i + 1]:
        count += arr[i] - arr[i+1]
        arr[i + 1] = arr[i]
    else:
        i += 1
print(count)

