from sys import *
input = stdin.readline
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = reversed(arr)
    one = 0
    two = 0
    if sum(arr) % x != 0:
        print(n)
    else:
        for k in arr:
            if k % x == 0:
                one += 1
            else:
                one += 1
                break
        for k in arr2:
            if k % x == 0:
                two += 1
            else:
                two += 1
                break
        if one == n:
            print(-1)
        else:
            print(n - min(one, two))