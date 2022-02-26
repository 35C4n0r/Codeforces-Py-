for _ in range(int(input())):
    n = int(input())
    count = 0
    c3 = 0
    c5 = 0
    c7 = 0
    if n % 3 == 0:
        print(n//3, 0, 0)
    elif n % 5 == 0:
        print(0, n//5, 0)
    elif n % 7 == 0:
        print(0, 0, n//7)
    elif n < 3:
        print(-1)
    else:
        while True:
            n = n//3


