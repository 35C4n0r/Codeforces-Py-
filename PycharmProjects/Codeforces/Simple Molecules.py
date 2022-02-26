n, m = list(map(int, input().split()))
arr = {}
arr2 = {}
for _ in range(m):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
        arr2[a] += 1
    else:
        arr[a] = [b]
        arr2[a] = 1
    if b in arr:
        arr[b].append(a)
        arr2[b] += 1
    else:
        arr[b] = [a]
        arr2[b] = 1
print(arr)
print(arr2)