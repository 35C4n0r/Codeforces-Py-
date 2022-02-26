n, m = list(map(int, input().split()))
met = {}
for _ in range(m):
    arr = list(map(int, input().split()))
    if _ == 0:
        met[arr[0]] = 1
        met[arr[1]] = 2
        met[arr[2]] = 3
    else:
        arr2 = [1, 2, 3]
        xxx = 0
        for k in range(3):
            if arr[k] in met:
                arr2.remove(met[arr[k]])
        for k in range(3):
            if arr[k] not in met:
                met[arr[k]] = arr2[xxx]
                xxx += 1
for kkk in range(1, n+1):
    print(met[kkk], end=' ')
