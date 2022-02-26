for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    if n%2 == 0:
        print(min(n*a,  (n // 2)*b))
    else:
        print(min((((n-1) // 2) * b) + a, n*a))