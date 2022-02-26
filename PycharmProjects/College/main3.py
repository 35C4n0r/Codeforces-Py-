'''num = int(input())
if num != 0:
    if num > 0:
        print("Number is greater than Zero")
    else:
        print("Number is less than Zero")'''
import math


def is_prime(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return i
    return 1


a = int(input())
b = int(input())
z = math.gcd(a, b)
res = is_prime(z)
if res == 1:
    print(1)
elif not res: 
    print("Second Greatest GCD Doesn't Exist")
else:
    print(z // res)