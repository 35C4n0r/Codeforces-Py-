from sys import *
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = n + arr[0] + arr[-1]
for k in range(1, n):
    ans += abs(arr[k-1] - arr[k])
print(ans)