# 1100
n = int(input())
arr = list(map(int, input().split()))
z = arr[0]
zz = arr[-1]
h = 0
hh = 0
for k in range(n - 1, 0, -1):
    if arr[k] != z:
        h = k
        break
for kk in range(n):
    if arr[kk] != zz:
        hh = kk
        break
if h == 0 and hh == 0:
    print(0)
    exit()
ans = max(h, n - hh - 1)
print(ans)