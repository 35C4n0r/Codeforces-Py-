
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []
    count = 1
    if n == 5:
        for k in arr:
            count *= k
        print(count)
    else:
        arr = sorted(arr)
        a = arr[0] * arr[1] * arr[2] * arr[3] * arr[4]
        b = arr[0] * arr[1] * arr[-1] * arr[-2] * arr[-3]
        c = arr[0] * arr[1] * arr[2] * arr[3] * arr[-1]
        d = arr[-1] * arr[-2] * arr[-3] * arr[-4] * arr[-5]
        result.append(a)
        result.append(b)
        result.append(c)
        result.append(d)
        print(max(result))

