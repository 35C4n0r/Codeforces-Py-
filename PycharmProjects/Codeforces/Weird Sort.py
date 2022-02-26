from sys import *
input = stdin.readline
for _ in range(int(input().strip())):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    p = list(map(int, input().split()))
    arr3 = [0]*n
    ans = True
    for i in p:
        arr3[i-1] = 1
    arr2 = arr.copy()
    arr2.sort()
    while True:
        g = False
        for k in range(n-1):
            if arr[k] > arr[k+1] and arr3[k] == 1:
                g = True
                arr[k], arr[k+1] = arr[k+1], arr[k]
                break
        if not g:
            break
    #print(arr, arr2, arr3, g)
    if arr == arr2:
        print("YES")
    else:
        print("NO")
