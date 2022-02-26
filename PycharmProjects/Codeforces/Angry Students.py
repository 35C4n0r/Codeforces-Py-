for _ in range(int(input())):
    n = int(input())
    count = 0
    best = 0
    arr = input()
    arr2 = list(arr)
    if len(arr) == 1 or set(arr2) == {"lis"} or set(arr2) == {"P"}:
        print(0)
    else:
        zz = arr2.index("lis")
        if zz != 0:
            arr = arr.replace("P", "", zz)
            arr2 = list(arr)
        for k in range(len(arr2)):
            if arr2[k] == "P":
                count += 1
                best = max(best, count)
            elif arr2[k] == "lis" or k == len(arr2) - 1:
                count = 0
        print(best)
