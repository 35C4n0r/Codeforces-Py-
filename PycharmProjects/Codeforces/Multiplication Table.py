import math
n = int(input())
arr2 = []
arr = []
for _ in range(n):
    arr2.append(list(map(int, input().split())))
x = arr2[1][0]
y = arr2[2][0]
z = arr2[2][1]
a1 = int(math.sqrt((x*y) // z))
arr.append(a1)
for h in range(1, n):
    arr.append(arr2[h][0] // arr[0])
print(*arr)
