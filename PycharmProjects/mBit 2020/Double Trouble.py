def removal(arr2, j):
    cunt = 0
    if arr2[0] == arr2[1] and arr2[0] != arr2[2]:
        arr2.pop(0)
    while cunt <= j:
        cunt += 1
        for kk in range(j, len(arr2) - 2):
            if arr2[kk] == arr2[kk+1] and arr2[kk] != arr2[kk-1] and arr2[kk] != arr2[kk+2]:
                arr2.pop(kk)
                j = kk
                break
    if arr2[-1] == arr2[-2] and arr2[-1] != arr2[-3]:
        arr2.pop(-1)


s = input()
arr = s.split()
#print(arr)
for k in arr:
    arr2 = list(k)
    if len(k) == 1:
        print(k, end=' ')
    elif len(k) == 2:
        if arr2[0] == arr2[1]:
            print(arr2[0], end=' ')
        else:
            print(k, end=' ')
    else:
        ans = []
        count = 0
        removal(arr2, 1)
        print(''.join(arr2), end=' ')
