import math
n = int(input())
arr = list(map(int, input().split()))
if len(set(arr)) == 1:
    xxx = (n*(n-1)) // 2
    print(0, xxx)
    exit()
x = max(arr)
y = min(arr)
diff = x - y
z = arr.count(x)
zz = arr.count(y)
ans = z * zz
print(diff, ans)
