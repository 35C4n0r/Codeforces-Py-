for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr3 = []
    arr4 = []
    for k in range(n):
        arr100 = list(map(int, input().split()))
        arr3.append(arr100)
    arr3.sort()
    for k in range(m):
        arr = list(map(int, input().split()))
    print(arr4, arr3)
    for kk in arr:
        for kkk in arr3:
            if kk in kkk:
                print(*kkk)
                arr3.remove(kkk)