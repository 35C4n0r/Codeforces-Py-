arr = []
for _ in range(3):
    arr2 = list(map(int, input().split()))
    for k in range(3):
        if arr2[k] == 0:
            arr2[k] = '1'
        else:
            arr2[k] = '0'
    arr.append(arr2)
for j in arr:
    print("".join(j))