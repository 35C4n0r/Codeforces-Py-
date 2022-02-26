n, t = list(map(int, input().split()))
arr = list(map(int, input().split()))
z = 1
while z:
    if z + arr[z-1] <= t:
        z += arr[z - 1]
    else:
        print("NO")
        exit()
    if z == t:
        print("YES")
        exit()