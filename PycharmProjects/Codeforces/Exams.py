from sys import *
input = stdin.readline
arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
arr.sort()
#print(abcd)
ans = 0
for kk in arr:
    if kk[1] >= ans:
        ans = kk[1]
    else:
        ans = kk[0]
print(ans)