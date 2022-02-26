arr = list(map(int, input().split()))
n = arr[0]
k = arr[1]
shelf1 = arr[2:n+2]
shelf2 = arr[n+2:]
z1 = max(shelf1)
z2 = max(shelf2)
while k > 0:
    if z2 > z1:
