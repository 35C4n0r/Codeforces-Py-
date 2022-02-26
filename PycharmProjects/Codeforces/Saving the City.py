for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    s = input()
    n = len(s)
    arr = list(map(int, list(s)))
    z = arr.count(1)
    cost1 = z * a
    arr2 = [arr[0]]
    for f in range(1, n):
        if arr[f] == 1 and arr[f - 1] != 1:
            arr2.append(1)
        elif arr[f] == 0:
            arr2.append(0)
    cnt = 0
    ans = 0
    for k in range(len(arr2)):
        if arr2[k] == 0:
            cnt += 1
        else:
            if ans == 0:
                ans = a
            else:
                ans = min(a+ans, ans + (cnt*b))
            cnt = 0
    print(ans)