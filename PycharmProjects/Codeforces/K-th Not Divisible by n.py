for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    z = (k-1)//(n-1)
    print(z+k)
