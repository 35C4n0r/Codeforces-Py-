n = int(input())
lis1 = []
lis2 = []
lis3 = []
arr = list(map(int, input().split()))
if n % 2 != 0:
    for i in range(0, n-1, 2):
        lis1.append(min(arr[i], arr[i+1]))
    lis1.append(arr[-1])
    arr.reverse()
    for j in range(0, n-1, 2):
        lis2.append(min(arr[j], arr[j+1]))
    lis2.append(arr[-1])
    print(min(sum(lis2), sum(lis1)))
else:
    for k in range(0, n - 1, 2):
        lis3.append(min(arr[k], arr[k + 1]))
    print(sum(lis3))



