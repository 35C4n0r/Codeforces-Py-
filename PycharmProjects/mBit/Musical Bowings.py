n = int(input())
arr = list(map(str, input().split()))
for k in range(n - 1):
    if arr[k] == 'B':
        if arr[k+1] == 'U':
            if arr[k-1] == 'B':

            arr[k] = 'D'
        else:
            arr[k] = 'U'
    if arr[n - 1] == 'B':
        if arr[n-2] == 'D':
            arr[n-1] = 'U'
        else:
            arr[n-1] = 'D'
print(*arr)