for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = list(set(arr))
    arr.sort()
    arr2.sort()
    count = 8
    if 0 not in arr:
        print(0)
        count = 7
    elif arr.count(0) == 1:
        for k in range(len(arr2) - 1):
            if arr2[k + 1] != arr2[k] + 1:
                print(arr2[k]+1)
                count = 1
                break
    else:
        for k in arr2:
            if arr.count(k) > 2:
                print(arr2[arr2.index(k)]+1+k+1)
                count = 6
                break
    if count == 8:
        print(max(arr2) + 1)