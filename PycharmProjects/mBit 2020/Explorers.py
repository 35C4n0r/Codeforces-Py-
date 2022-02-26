from sys import *
input = stdin.readline
n, m = list(map(int, input().split()))
zheng = []
yang = []
ans = []
for i in range(n-1, -1, -1):
    x = range(0, m) if (i%2 == 1) else range(m-1, -1, -1)
    for j in x:
        zheng.append([i, j])
for j in range(m):
    x = range(0, n) if (j%2 == 0) else range(n-1, -1, -1)
    for i in x:
        yang.append([i, j])
#print(zheng)
#print(yang)
for kk in range(n*m):
    if zheng[kk] == yang[kk]:
        ans.append(kk + 1)
print(len(ans))
print(*ans)
