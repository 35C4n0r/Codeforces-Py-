from sys import *
input = stdin.readline
n, m = list(map(int, input().split()))
reality = list(map(int, input().split()))
betting = list(map(int, input().split()))
reality.sort()
reality.reverse()
for k in betting:
    for j in reality:
        if k < reality[-1]:
            print(-1)
            break
        else:
            if j <= k:
                print(j)
                reality.remove(j)
                break
