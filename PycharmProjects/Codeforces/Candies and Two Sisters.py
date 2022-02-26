for _ in range(int(input())):
    n = int(input())
    if n % 2 != 0:
        print((n//2))
    elif n == 0:
        print(0)
    else:
        print((n//2)-1)
