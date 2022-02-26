import math
n = int(input())
arr = list(map(int, input().split()))
count = 0
num = 0
arr100 = []
arr3 = set(arr)
if len(set(arr)) == 1:
    print(0)
else:
    for k in arr3:
        z = arr.count(k)
        if z > count:
            count = z
            num = k
    for k in range(arr.index(num), len(arr) - 1):
        if arr[k] == num and arr[k+1] == num:
            continue
        elif arr[k] == num:

            if num > arr[k+1]:
                arr100.append(f'1 {k + 2} {k + 1}')
                arr[k + 1] = arr[k]
            else:
                arr100.append(f'2 {k + 2} {k + 1}')
                arr[k + 1] = arr[k]
        elif arr[k+1] == num:
            if num > arr[k]:
                arr100.append(f'1 {k + 1} {k + 2}')
                arr[k] = arr[k + 1]
            else:
                arr100.append(f'2 {k + 1} {k + 2}')
                arr[k] = arr[k + 1]

    for kkk in range(arr.index(num), -1, -1):
        if arr[kkk] == num and arr[kkk-1] == num:
            continue
        elif arr[kkk] == num:
            #print(lis[kkk], lis[kkk-1], num)
            if num > arr[kkk-1]:
                arr100.append(f"1 {kkk} {kkk + 1}")
                arr[kkk - 1] = arr[kkk]
            else:
                arr100.append(f"2 {kkk} {kkk + 1}")
                arr[kkk - 1] = arr[kkk]
    print(len(arr100))
    for zz in arr100:
        print(zz)

