from sys import *
import math
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        print(0)
    elif len(arr) - len(set(arr)) == 0:
        print(1)
    else:
        