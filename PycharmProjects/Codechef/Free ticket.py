from sys import *
input = stdin.readline
'''c, f = list(map(int, input().split()))
arr = {}
for _ in range(f):
    x, y, p = list(map(int, input().split()))
    if x not in arr:
        arr[x] = [y]
    else:
        arr[x].append(y)
    if y not in arr:
        arr[y] = [x]
    else:
        arr[y].append(x)
print(arr)'''
# cook your dish here
c, f = [int(x) for x in input().split()]
A = [[0 for i in range(c)] for i in range(c)]
print(A)
for i in range(f):
    x, y, p = [int(x) for x in input().split()]
    A[x - 1][y - 1] = p
    A[y - 1][x - 1] = p
print(A)
n = c
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
m = float('-inf')
for i in A:
    m = max(max(i), m)

print(m)
