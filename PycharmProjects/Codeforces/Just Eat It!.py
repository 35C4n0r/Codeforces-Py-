for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if max(arr) >= sum(arr):
        print("NO")
        continue
    dp = [0]*(n+1)
    flag = False
    ans = 0
    for i in range(1, n+1):
        dp[i] = max(arr[i-1], dp[i-1] + arr[i-1])
        if i != 1 and (dp[i] == arr[i-1] or dp[i] == 0):
            flag = True
    dp.sort()
    ans = dp[-2]
    if flag:
        ans = dp[-1]
    if ans >= sum(arr):
        print("NO")
    else:
        print("YES")