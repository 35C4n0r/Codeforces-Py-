n = int(input())
arr = list(map(int, input().split()))
sum = 0
z = 0
while z + 2 <= n:
    zz = min(arr[z], arr[z + 1], arr[z+2])
    if zz == arr[z + 2]:
        z = z + 3
    elif zz == arr[z+1]:
        z = z + 2
    else:
        z = z + 1
    sum += zz
print(sum)