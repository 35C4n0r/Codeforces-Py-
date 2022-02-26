for _ in range(int(input())):
    n = int(input())
    mx = 0
    dm = True
    arr = list(map(int, input().split()))
    arr2 = arr.copy()
    arr2.sort()
    if len(set(arr)) == 1:
        print("NO")
    else:
        print("YES")
        for k in arr2:
            if k != arr[0]:
                x = k
            if arr.count(k) == 1:
                dm = False
                zzz = arr.index(k)
                for kk in range(0, n):
                    if kk != zzz:
                        print(zzz + 1, kk + 1)
                break
        if dm:
            mm = arr.index(x)
            print(1, mm + 1)
            for hj in range(0, n):
                if arr[hj] != arr[0]:
                    if (hj+1, 1) != (mm+1, 1):
                        print(hj+1, 1)
                else:
                    if (mm+1, hj+1) != (mm + 1, 1):
                        print(mm + 1, hj + 1)
