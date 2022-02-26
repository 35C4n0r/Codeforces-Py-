import math
from sys import *
input = stdin.readline
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a < b:
        print(0)
    else:
        print(math.ceil(a / b))