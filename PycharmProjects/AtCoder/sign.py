'''n = int(input())
arr = list(map(int, input().split()))
count = 0
arr2 = []
arr3 = []
arr4 = []
arr5 = []
if len(set(arr)) == 1:
    print()
else:
    for k, kk in zip(range(0, n, 2), range(1, n, 2)):
        arr2.append(arr[k])
        arr4.append(arr.count(arr[k]))
        arr3.append(arr[kk])
        arr5.append(arr.count(arr[kk]))
    z = max(arr4)
    zz = arr2[arr4.index(z)]
    d = max(arr5)
    dd = arr3[arr5.index(d)]
    while zz == dd:
        arr[]
'''