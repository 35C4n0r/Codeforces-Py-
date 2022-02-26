from sys import *
input = stdin.readline
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = [0]*(n+1)
ans = 1
for k in range(n):
    arr2[arr[k]] = k
arr2.remove(0)
for j in range(n - 1):
    if arr2[j] > arr2[j+1]:
        ans += 1
print(ans)

