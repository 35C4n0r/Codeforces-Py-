fin = open('bcount.in', 'r')
fout = open('bcount.out', 'w')
n, q = list(map(int, fin.readline().split()))
arr = []
arr1 = [0]*(n+1)
arr2 = [0]*(n+1)
arr3 = [0]*(n+1)
for _ in range(n):
    j = int(fin.readline())
    arr.append(j)
    arr1[_+1] = arr1[_]
    arr2[_+1] = arr2[_]
    arr3[_+1] = arr3[_]
    if j == 1:
        arr1[_+1] += 1
    elif j == 2:
        arr2[_+1] += 1
    else:
        arr3[_+1] += 1
print(arr1, arr2, arr3, arr)
for i in range(q):
    a, b = list(map(int, fin.readline().split()))
    fout.write(str(arr1[b] - arr1[a - 1]) + ' ' + str(arr2[b] - arr2[a - 1]) + ' ' + str(arr3[b] - arr3[a - 1]) + '\n')
fout.close()