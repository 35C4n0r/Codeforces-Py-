# cook your dish here
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
count = 0
z = n - 1
zz = n - 2
picked = True
while zz >= 0 and z >= 0:
    print(z, zz)
    if arr[z] - arr[zz] >= k:
        count += zz + 1
        z -= 1
        zz = z - 1
    elif arr[z] - arr[zz] < k:
        zz -= 1
print(count + 1)