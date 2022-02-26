import numpy as np
from collections import *
import math


def prime_factor(num):
    ans = []
    while num % 2 == 0:
        ans.append(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            ans.append(i)
            num //= i
    if num > 2:
        ans.append(num)
    return ans


a, b = list(map(int, input().split()))
arr = prime_factor(a)
arr2 = prime_factor(b)
#print(arr, arr2)
arr = np.array(arr)
arr2 = np.array(arr2)
commomon_prime_factors_of_a_and_b = np.intersect1d(arr, arr2)
gcd_a_b = np.product(commomon_prime_factors_of_a_and_b)
print(gcd_a_b)