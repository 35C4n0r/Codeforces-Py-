n = int(input())
M = 1000000007


def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x % M
    sqrt = power(x, n // 2)
    mul = x if n % 2 == 1 else 1

    return (mul * sqrt * sqrt) % M


print(power(2, n))
