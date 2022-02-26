for _ in range(int(input())):
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    arr10 = []
    for k in range(n):
        if arr[k] == 1:
            arr10.append(k)
    for k in range(len(arr10) - 1):
        count += arr10[k + 1] - arr10[k] - 1
    #print(arr10)
    print(count)
