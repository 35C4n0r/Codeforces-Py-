n = int(input())
x = ((n*(n-1)) // 2) - 1
arr = {}
arr2 = {}
arr3 = []
for _ in range(x):
    a, b = map(int, input().split())
    if a in arr:
        arr[a].append(b)
    else:
        arr[a] = [b]
    if a in arr2:
        arr2[a].append(b)
    else:
        arr2[a] = [b]
    if b in arr2:
        arr2[b].append(a)
    else:
        arr2[b] = [a]
#print(lis)
#print(arr1000)
count = 0
for k in arr2:
    if len(arr2[k]) == n - 2:
        arr3.append(k)
        count += 1
    if count == 2:
        break
u, v = arr3
if u in arr and v in arr:
    if len(arr[u]) > len(arr[v]):
        print(u, v)
    else:
        print(v, u)
else:
    if u in arr:
        print(u, v)
    else:
        print(v, u)