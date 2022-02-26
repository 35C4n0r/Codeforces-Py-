n, k = list(map(int, input().split()))
arr = [k for k in range(1, n+1)]
arr2 = arr.copy()
for _ in range(k):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr.remove(a)
    if b in arr:
        arr.remove(b)
z = arr[0]
arr2.remove(z)
print(n - 1)
for kk in arr2:
    print(z, kk)
