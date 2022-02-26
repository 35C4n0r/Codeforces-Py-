n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(2 * n):
    if arr[i] == 0:
        continue
    for j in range(i + 1, 2 * n):
        if arr[i] == arr[j]:
            arr[j] = 0
            break
        count += (arr[j] > 0)
print(count)