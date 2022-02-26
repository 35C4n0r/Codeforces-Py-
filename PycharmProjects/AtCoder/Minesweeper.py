h, w = list(map(int, input().split()))
arr = []
arr2 = []
arr100 = []
xx = [0] * w
for _ in range(h):
    arr2.append(list(map(str, list(input()))))
    arr.append(xx)
print(arr2)
print(arr)
for k in range(h):
    #print(k, arr)
    if k == 0:
        for j in range(w):
            if arr2[k][j] == '#':
                print(100)
                arr[k+1][j] += 1
                if j > 0:
                    arr[k+1][j-1] += 1
                    arr[k][j-1] += 1
                if j != w-1:
                    arr[k][j+1] += 1
                    arr[k+1][j+1] += 1
                #arr[k][j] = '#'
                arr100.append((k, j))
    elif k == h-1:
        for j in range(w):
            if arr2[k][j] == '#':
                print(100)
                arr[k - 1][j] += 1
                if j > 0:
                    arr[k - 1][j - 1] += 1
                    arr[k][j - 1] += 1
                if j != w - 1:
                    arr[k][j + 1] += 1
                    arr[k - 1][j + 1] += 1
                #arr[k][j] = '#'
                arr100.append((k, j))
    else:
        for j in range(w):
            if arr2[k][j] == '#':
                print(k, j)
                if j != w-1:
                    arr[k][j+1] = 1
                    arr[k+1][j+1] += 1
                    arr[k-1][j+1] += 1
                    print(arr, k)
                    print(arr[k][j+1])
                    print(arr[k+1][j+1])
                    print(arr[k-1][j+1])
                if j > 0:
                    arr[k][j-1] += 1
                    arr[k+1][j-1] += 1
                    arr[k-1][j-1] += 1
                    print(arr, k)
                arr[k+1][j] += 1
                arr[k-1][j] += 1
                print(arr, k)

for nd in arr100:
    print(nd)
    #arr[nd[0]][nd[1]] = '#'
