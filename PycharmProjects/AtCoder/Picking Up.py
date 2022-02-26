n = int(input())
arr = []
arr3 = []
zz = (n*(n-1)) // 2
arr4 = [0] * zz
for _ in range(n):
    arr.append(list(map(int, input().split())))
if n == 1:
    print(1)
    exit()
arr.sort()
for k in range(n - 1):
    for kk in range(k + 1, n):
        if [arr[k][0] - arr[kk][0], arr[k][1] - arr[kk][1]] not in arr3:
            arr3.append([arr[k][0] - arr[kk][0], arr[k][1] - arr[kk][1]])
            arr4[arr3.index([arr[k][0] - arr[kk][0], arr[k][1] - arr[kk][1]])] += 1
        else:
            arr4[arr3.index([arr[k][0] - arr[kk][0], arr[k][1] - arr[kk][1]])] += 1
x = max(arr4)
print(n - x)