for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    if n == 1 or n == 2:
        print(1)
    else:
        count = int(((n-3)/x)+1)
        print(count + 1)