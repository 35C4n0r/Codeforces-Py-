M = 1000000007


'''def power(X, N):
    if N == 0:
        return 1
    elif N == 1:
        return X % M
    SQRT = power(X, N // 2)
    if N % 2 == 1:
        mul = X
    else:
        mul = 1
    return (mul * SQRT * SQRT) % M'''


'''for _ in range(int(input())):
    X, N = list(map(int, input().split()))
    z = ((X ** N) % M) % M
    print(z)'''
