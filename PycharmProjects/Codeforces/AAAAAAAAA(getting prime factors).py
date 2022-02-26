import math


def prime_factors(n):
    global arr
    while n % 2 == 0:
        arr.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            arr.append(i)
            if i > 5:
                print(-1)
                exit()
            n = n // i
    if n > 2:
        arr.append(n)
        if n > 5:
            print(-1)
            exit()


arr = []
n = 15
prime_factors(n)
print(arr)