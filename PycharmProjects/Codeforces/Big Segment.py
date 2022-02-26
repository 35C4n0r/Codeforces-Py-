mi = 9999999999
ma = 0
arr2 = []
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    mi = min(mi, a)
    ma = max(ma, b)
    arr2.append((a, b))
if (mi, ma) in arr2:
    print(arr2.index((mi, ma)) + 1)
else:
    print(-1)