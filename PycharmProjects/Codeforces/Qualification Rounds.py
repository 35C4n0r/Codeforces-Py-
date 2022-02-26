import math
n, k = list(map(int, input().split()))
z = 0
arr2 = [0]*n
arr4 = {}
arr3 = 0
count = 0
f = False
for _ in range(n):
    arr = list(map(int, input().split()))
    for kk in range(k):
        if arr[kk] == 1:
            arr2[kk] += 1
        if arr2[kk] > math.ceil(n / 2):
            print("NO")
            exit()
print("YES")