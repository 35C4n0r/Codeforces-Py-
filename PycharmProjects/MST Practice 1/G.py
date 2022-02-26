for _ in range(int(input())):
    useless = input()
    n = int(input())
    arr = []
    for k in range(n):
        arr.append(list(map(float, input().split())))
    arr2 = []
    for k in range(n):
        for kk in range(k + 1, n):
            print(k, kk)

