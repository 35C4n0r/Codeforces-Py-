for _ in range(int(input())):
    n = int(input())
    arr = []
    arr100 = []
    for _ in range(n):
        arr.append(list(input()))
    #print(lis)
    z = n // 2
    zz = z-1
    zzz = z+1
    arr1 = arr[zz]
    arr2 = arr[z]
    arr3 = arr[zzz]
    for kk in range(n):
        if arr1[kk] == '1':
            arr100.append([zz, kk])
        if arr2[kk] == '0':
            arr100.append([z, kk])
        if arr3[kk] == '1':
            arr100.append([zzz, kk])
    print(len(arr100))
    for k in arr100:
        print(*k)
