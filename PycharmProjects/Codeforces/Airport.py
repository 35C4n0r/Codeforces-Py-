n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
z = sum(arr)
if z <= n:
    print(z, z)
else:
    if len(arr) > n:
        print
    for k in range(n):
