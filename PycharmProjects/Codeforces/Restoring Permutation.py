for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    for i in arr:
        arr2.append(i)
        t = i+1
        while t in arr or t in arr2:
            t += 1
        arr2.append(t)
    if max(arr2) == 2 * n:
        print(*arr2)
    else:
        print("-1")
