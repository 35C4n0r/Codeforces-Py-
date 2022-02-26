n = int(input())
s = input()
count = 0
arr = list(s)
for k in range(1, n - 1):
    arr3 = ['R', 'B', 'G']
    if arr[k] == arr[k-1]:
        count += 1
        if arr[k] == 'R':
            if arr[k+1] == 'R':
                arr[k] = 'G'
            if arr[k+1] == 'G':
                arr[k] = 'B'
            if arr[k+1] == 'B':
                arr[k] = 'G'
        if arr[k] == 'G':
            if arr[k+1] == 'R':
                arr[k] = 'B'
            if arr[k+1] == 'G':
                arr[k] = 'B'
            if arr[k+1] == 'B':
                arr[k] = 'R'
        if arr[k] == 'B':
            if arr[k+1] == 'R':
                arr[k] = 'G'
            if arr[k+1] == 'G':
                arr[k] = 'R'
            if arr[k+1] == 'B':
                arr[k] = 'G'
    if arr[n-1] == arr[n-2]:
        count += 1
        if arr[n - 2] == 'R':
            arr[n - 1] = 'G'
        if arr[n - 2] == 'G':
            arr[n - 2] = 'B'
        if arr[n - 1] == 'B':
            arr[n - 2] = 'G'
print(count)
print(''.join(arr))