from sys import *
input = stdin.readline
import math
n, m = list(map(int, input().split()))
arr = [[0 for i in range(5)] for j in range(m)]
#print(lis)
#lis[1][2] += 1
#print(lis[0], lis[1][2])
for _ in range(n):
    arr2 = list(input())
    #print(arr2)
    for k in range(m):
        #print(k, arr2[k])
        if arr2[k] == 'A':
            arr[k][0] += 1
        elif arr2[k] == 'B':
            arr[k][1] += 1
        elif arr2[k] == 'C':
            arr[k][2] += 1
        elif arr2[k] == 'D':
            arr[k][3] += 1
        elif arr2[k] == 'E':
            arr[k][4] += 1
        #print()
ans = 0
#print(lis)
arr3 = list(map(int, input().split()))
for jj in range(m):
    ans += arr3[jj] * max(arr[jj])
    #print(ans)
print(ans)