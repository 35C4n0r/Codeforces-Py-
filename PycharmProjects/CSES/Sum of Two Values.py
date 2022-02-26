n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = arr.copy()
arr.sort()
count = 0
i = 0
j = n - 1
while j > i:
    if arr[i] + arr[j] == x:
        count += 1
        if arr[i] == arr[j]:
            a = arr2.index(arr[j]) + 1
            arr2.remove(arr[j])
            b = arr2.index(arr[i]) + 2
            print(a, b)
        else:
            a = arr2.index(arr[j]) + 1
            b = arr2.index(arr[i]) + 1
            print(a, b)
        break
    else:
        if arr[j] + arr[i] >= x:
            j -= 1
        else:
            i += 1
if count == 0:
    print("IMPOSSIBLE")