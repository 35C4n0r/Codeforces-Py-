n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
time = 0
arr.sort(reverse=True)
print(arr)
while min(arr) < x:
    z = x - arr[0]
    y = x - arr[1]
    xx = min(z, y)
    if xx == 0:
        if y == 0:
            arr[0] += z
            time += z
        else:
            arr[0] += y
            time += y
    else:
        arr[0] += xx
        arr[1] += xx
        time += xx
    #print(arr, time, 1234567890)
    arr.sort(reverse=True)
    #print(arr, z, y)
print(time)