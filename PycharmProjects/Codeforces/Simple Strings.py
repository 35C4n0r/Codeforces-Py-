from sys import *
input = stdin.readline
print = stdout.write
s = input().strip()
arr = list(s)
arr2 = list('abcdefghijklmnopqrstuvwxyz')
s = {}
for j in range(26):
    s[arr2[j]] = j
#print(s)
pre = 0
curr = s[arr[0]]
post = 0
for k in range(len(arr) - 1):
    curr = s[arr[k]]
    if k != 0:
        pre = s[arr[k-1]]
    post = s[arr[k+1]]
    #print(curr, post, pre, k)
    if curr == post:
        for jj in range(26):
            if jj != post and jj != pre:
                arr[k] = arr2[jj]
                break
print(''.join(arr))
