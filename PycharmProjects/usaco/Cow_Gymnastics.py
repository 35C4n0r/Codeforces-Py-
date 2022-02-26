"""
ID: jay20ma1
LANG: PYTHON3
TASK: gymnastics
"""
fin = open('gymnastics.in', 'r')
fout = open('gymnastics.out', 'w')
k, n = list(map(int, fin.readline().split()))
arr = []
arr2 = [[0 for _ in range(20)] for __ in range(20)]
ans = 0
for i in range(k):
    arr.append(list(map(int, fin.readline().split())))
    for _ in range(n):
        for __ in range(_+1, n):
            arr2[arr[i][_] - 1][arr[i][__] - 1] = True
for i in range(n):
    for j in range(i+1, n):
        if not arr2[i][j] or not arr2[j][i]:
            ans += 1
fout.write(str(ans))