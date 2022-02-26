n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
count = 0
z = 0
zz = n - 1
while z != zz:
    if arr[z] + arr[zz] >= k:
        zz -= 1
    elif arr[z] + arr[zz] < k:
        count += zz - z
        z += 1
print(count)