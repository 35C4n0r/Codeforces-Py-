from sys import *
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2 = {}
i = 0
ans = 0
for j in range(n):
    #print(i, j, arr2)
    if arr[j] in arr2:
        #print(arr2[arr[j]] + 1, i, 'll')
        i = max(arr2[arr[j]] + 1, i)
        #i = arr[arr[j]] + 1
    ans = max(ans, j - i + 1)
    arr2[arr[j]] = j
print(ans)