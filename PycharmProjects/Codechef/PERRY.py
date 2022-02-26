for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = False
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cost = 0
    for k, kk in zip(range(n - 1), range(n - 1)):
        if 