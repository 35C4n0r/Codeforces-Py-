import math
n = int(input())
for _ in range(int(n)):
    arr = list(input())
    res = 0
    cur = 0
    for k in range(len(arr)):
        if arr[k] == '+':
            cur += 1
        else:
            cur -= 1
        if cur < 0:
            res += 1
            cur += 1
            ok = False
            break
    print(res)

