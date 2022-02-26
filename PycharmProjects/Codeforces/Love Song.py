from sys import *
input = stdin.readline
print = stdout.write
n, q = list(map(int, input().split()))
s = input()
arr = list(s)
alpha = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for i in range(26):
    d[alpha[i]] = i+1
for j in range(n):
    if j != 0:
        arr[j] = d[arr[j]] + arr[j-1]
    else:
        arr[j] = d[arr[j]]
#print(arr)
for k in range(q):
    l, r = list(map(int, input().split()))
    if l >= 2:
        ans = arr[r-1] - arr[l-2]
    else:
        ans = arr[r-1]
    print(str(ans) + '\n')
