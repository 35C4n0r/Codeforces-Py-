"""
ID: jay20ma1
LANG: PYTHON3
TASK: socdist1
"""
import math
fin = open('socdist1.in', 'r')
fout = open('socdist1.out', 'w')
mx = 0
mn = math.inf
arr10 = []
n = int(fin.readline())
arr = list(map(int, list(fin.readline().strip('\n'))))
for k in range(n):
    if arr[k] == 1:
        arr10.append(k)
for kk in range(len(arr10) - 1):
    mn = min(mn, abs(arr10[kk] - arr10[kk+1]) - 1)
    mx = max(mx, abs(arr10[kk] - arr10[kk+1]) - 1)
#print(mn, mx, arr10)
fout.write(f'{min(mn, math.ceil(mx / 2))}')
fout.write('\n')
fout.close()
