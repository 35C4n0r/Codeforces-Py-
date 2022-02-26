import math


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


a = int(input())
b = int(input())
while a <= b:
    if is_prime(a):
        print(a, end=' ')
    a += 1
