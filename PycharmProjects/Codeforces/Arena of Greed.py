for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 0:
        if n % 2 == 0 and (n//2) % 2 == 1 or n == 4:
            count += n//2
            n = n//2
            n -= 1
        else:
            count += 1
            n -= 1
            n = n//2
    print(count)
