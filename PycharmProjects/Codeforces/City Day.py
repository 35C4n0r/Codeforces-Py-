from sys import *
input = stdin.readline
n, x, y = list(map(int, input().split()))
arr = list(map(int, input().split()))
for kk in range(n):
    m = max(0, kk - x)
    mm = min(n, kk + y)
    arr2 = arr[m:mm+1]
    #print(arr2)
    if min(arr2) == arr[kk]:
        print(kk+1)
        exit()