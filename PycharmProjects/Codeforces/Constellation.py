import math
from sys import *
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    a, b, c = list(map(int, input().split()))
    z = math.ceil(n/2)
    win = 0
    arr = list(map(str, list(input())))
    arr3 = []
    for k in arr:
        if k == 'R' and b > 0:
            b -= 1
            win += 1
            arr3.append('P')
        elif k == 'P' and c > 0:
            c -= 1
            win += 1
            arr3.append('S')
        elif k == 'S' and a > 0:
            a -= 1
            win += 1
            arr3.append('R')
        else:
            arr3.append('@')
        if a == 0 and b == 0 and c == 0:
            break
    if win >= z:
        print("YES")
        for tt in arr3:
            if tt == '@':
                if a>0:
                    print('R', end='')
                    a-=1
                elif b>0:
                    print('P', end='')
                    b-=1
                elif c>0:
                    print("S", end='')
                    c-=1
            else:
                print(tt, end='')
        print()

    else:
        print("NO")