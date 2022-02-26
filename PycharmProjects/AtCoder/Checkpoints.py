import math
n, m = list(map(int, input().split()))
arr = []
arr2 = []
arr3 = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for _ in range(m):
    arr2.append(list(map(int , input().split())))
for k in arr:
    count = math.inf
    ind = 0
    for j in range(m):
        #arr3.append(abs(k[0] - j[0]) + abs(k[1] - j[1]))
        #print(abs(k[0] - arr2[j][0]) + abs(k[1] - arr2[j][1]))
        if abs(k[0] - arr2[j][0]) + abs(k[1] - arr2[j][1]) < count:
            ind = j
            count = abs(k[0] - arr2[j][0]) + abs(k[1] - arr2[j][1])
    print(ind + 1)
