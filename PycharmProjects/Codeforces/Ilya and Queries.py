from sys import *
input = stdin.readline
s = input()
arr = list(s)
n = int(input())
arr2 = [0]
cc = 0
for k in range(1, len(arr)):
    if arr[k] == arr[k-1]:
        cc += 1
    arr2.append(cc)
for _ in range(n):
    a, b = list(map(int, input().split()))
    count = arr2[b-1] - arr2[a-1]
    print(count)
