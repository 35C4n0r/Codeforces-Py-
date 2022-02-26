n = int(input())
arr = list(map(int, input().split()))
arr3 = []
for k in range(1, n+1):
    #print(k)
    arr2 = []
    z = k
    while k:
        if k in arr2:
            #print(arr1000)
            arr3.append(k)
            break
        else:
            arr2.append(k)
            k = arr[k-1]
print(*arr3)