import math
n, d, h = list(map(int, input().split()))
arr = []
m = 0
mm = math.inf
arr2 = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    arr.append([a, b])
arr.sort()
#print(lis)
for j in arr:
    m = (h - j[1]) / (d - j[0])
    #print(m)
    mm = min(m, mm)
#print(mm)
c = h - mm*d
if c < 0:
    print(0.000)
else:
    print(c)