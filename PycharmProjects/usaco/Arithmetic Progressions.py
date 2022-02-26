"""
ID: jay20ma1
LANG: PYTHON3
TASK: ariprog
"""
import itertools
ant2 = -1
fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')
n = int(fin.readline())
k = int(fin.readline())
arr = []
arr2 = {}
for j in range(k+1):
    for jj in range(k+1):
        ant = (j**2)+(jj**2)
        if ant not in arr:
            arr.append(ant)
z = len(arr)
arr.sort()

'''for h in itertools.combinations(arr, n):
    print(h)
    mf = h[1] - h[0]
    ml = h[-1] - h[-2]
    mb = h[n//2 +1] - h[n//2]
    if mf == ml == mb:
        print(h[0], ml)
    if mm in arr2:
        arr2[mm].append(h[0])
        if h[0] not in arr2[mm]:
            arr2[mm].append(h[1])
    else:
        arr2[mm] = [h[0], h[1]]
print(arr)
print(arr2)'''