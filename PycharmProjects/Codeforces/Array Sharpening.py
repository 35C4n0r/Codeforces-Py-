for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    first = True
    second = True
    if arr.count(0) > 2:
        print("No")
    else:
        z = max(arr)
        zz = arr.index(z)
        for k in range(zz + 1, n):
            if z <= arr[k] or arr[k - 1] <= arr[k]:
                arr[k] = arr[k-1] - 1
                if arr[k] < 0:
                    print("No")
                    first = False
                    break

        if first:
            for k in range(zz - 1, -1, -1):
                if z <= arr[k] or arr[k + 1] <= arr[k]:
                    arr[k] = arr[k + 1] - 1
                    if arr[k] < 0:
                        print("No")
                        second = False
                        break
        print(first, second, arr, zz)
        if first and second:
            print("Yes")
