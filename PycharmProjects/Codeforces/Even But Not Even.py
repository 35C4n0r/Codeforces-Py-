# 900
for _ in range(int(input())):
    n = int(input())
    result = []
    count = 0
    arr = int(input())
    arr2 = list(str(arr))
    arr2 = list(map(int, arr2))
    for k in arr2:
        if len(result) == 2:
            break
        elif k % 2 != 0:
            result.append(k)
            count += 1

    result = list(map(str, result))
    if count == 0 or len(result) == 1:
        print(-1)
    else:
        print("".join(result))
