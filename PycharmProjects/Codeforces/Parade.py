from sys import *
input = stdin.readline
n = int(input())
arr = []
arr2 = []
l = 0
r = 0
for _ in range(n):
    ll = list(map(int, input().split()))
    arr.append(ll)
    arr2.append([ll[1], ll[0]])
    l += ll[0]
    r += ll[1]
bu = abs(l-r)
ans = 0
for i in range(n):
    a, b = arr[i][0], arr[i][1]
    smh = abs((l - a + b) - (r - b + a))
    if smh > bu:
        bu = smh
        ans = i+1
print(ans)