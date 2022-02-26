for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = list(set(arr))
    if arr2 == [0]:
        print(0)
        exit()
    z = arr2.count(0)
    if z != 0:
        arr2.remove(0)
    arr.sort()
    print(len(arr2))

