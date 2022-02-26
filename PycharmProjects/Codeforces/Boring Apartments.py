for _ in range(int(input())):
    n = input()
    arr10 = list(map(int, list(n)))
    #print(arr10)
    n = int(n)
    arr = [i for i in range(1, len(arr10) + 1)]
    #print(lis)
    print((10 * (arr10[0] - 1)) + sum(arr))