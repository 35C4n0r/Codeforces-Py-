'''from sys import *
input = stdin.readline'''
n, zz = list(map(int, input().split()))
arr = []
xx = 0
for _ in range(n):
    s, t, w = list(map(int, input().split()))
    xx = max(xx, w)
    arr.append([t, w, s])
arr2 = [0]*(xx+1)
arr.sort()
print(w)
for kk in arr:
    for jj in range(kk[0], kk[1] + 1):
        arr2[jj] += 1
        print(arr2[jj])
        if arr2[jj] > zz:
            print("NO")
            exit()
print(arr2)
print("YES")