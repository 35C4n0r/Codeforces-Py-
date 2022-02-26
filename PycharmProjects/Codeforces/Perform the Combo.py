from collections import Counter
from sys import *
input = stdin.readline
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
pos = list(map(int, input().split()))
s = 'abcdefghijklmnopqrstuvwxyz'
arr2 = list(s)
mep = {}
for k in range(26):
    mep[k] = k
#print(arr2)
arr3 = [0] * 26
for j in pos:
    arr3[j-1] += 1
