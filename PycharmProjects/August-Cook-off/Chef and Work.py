for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    count = 0
    flag = 1
    for i in range(n):
        if w[i] > k:
            flag = 0
            break
        elif count + w[i] <= k:
            count += w[i]
        else:
            flag += 1
            count = w[i]
    if flag == 0:
        print("-1")
    else:
        print(flag)