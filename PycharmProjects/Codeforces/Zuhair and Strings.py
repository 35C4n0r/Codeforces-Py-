n, kk = list(map(int, input().split()))
l = input()
arr = list(l)
arr2 = list(set(arr))
count = 0
best = 0
for k in arr2:
    xx = [k]*kk
    x = "".join(xx)
    count = max(count, l.count(x))
print(count)
#TLE