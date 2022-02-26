# 1100
n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
z = n-1
zz = x - sum(arr)
if zz == z:
    print("YES")
else:
    print("NO")