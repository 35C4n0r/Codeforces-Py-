for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = arr.copy()
    arr4 = []
    x = 0
    if 1 in arr2:
        x = arr2.count(1)
    while x > 0:
        arr3.remove(arr[arr2.index(1)])
        arr4.append(arr2.index(1))
        arr2.insert(arr2.index(1), "@")
        arr2.pop(arr2.index(1))
        x -= 1
    arr3.sort()
    for k in arr4:
        arr3.insert(k, arr[k])
    for kk in arr3:
        print(kk, end=" ")
    print()


