n, m, k = list(map(int, input().split()))
arrn = list(map(int, input().split()))
arrm = list(map(int, input().split()))
arr = [[]]*m
print(arr)
for j in arrn:
    for jj in range(m):
        print(j, arrm[jj])
        arr[jj].append(arrm[jj]*j)
print(arr)