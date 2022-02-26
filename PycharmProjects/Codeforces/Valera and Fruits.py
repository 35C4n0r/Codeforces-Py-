n, v = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
curr = 0
pre = 0
for k in arr:
    if k[1] > v:
        xd = (k[1] + pre) - v
        curr += v
        pre = 0
        pre += k[1] - v
    else:
        curr += (k[1] + pre) - v

    print(pre, curr, k)
print(curr)
