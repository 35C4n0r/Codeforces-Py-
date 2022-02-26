for _ in range(int(input())):
    arr = list(input())
    count = 0
    ans = 0
    for k in range(len(arr)):
        if arr[k] == 'L':
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print(ans + 1)