n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0
for k in range(1, n+1):
    if k in arr:
        arr.remove(k)
    else:
        count += abs(arr[0] - k)
        arr.pop(0)
print(count)