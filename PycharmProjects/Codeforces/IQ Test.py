arr = []
for _ in range(4):
    arr.append(list(input()))
for k in range(3):
    for kk in range(3):
        arr100 = []
        arr100.append(arr[k][kk])
        arr100.append(arr[k][kk+1])
        arr100.append(arr[k+1][kk])
        arr100.append(arr[k+1][kk+1])
        zz = arr100.count('#')
        zzz = arr100.count('.')
        if (zz == 4) or (zzz == 4) or (zz == 3 and zzz == 1) or (zz == 1 and zzz == 3):
            print("YES")
            exit()
print("NO")