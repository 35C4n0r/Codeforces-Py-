from sys import *
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0
abe = 0
for _ in range(2):
    for kk in range(1, n+1):
        z = arr.index(kk)
        ans += abs(abe - z)
        abe = z
        arr[z] = '@'
print(ans)