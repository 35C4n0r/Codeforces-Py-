'''from collections import deque
from sys import *
input = stdin.readline
s = input().strip()
arr = list(s)
arr2 = []
pen15 = True
for k in arr:
    if k != 'R':
        arr2.append(k)
    else:
        arr2.reverse()
    if len(arr2) > 2:
        if arr2[-1] == arr2[-2]:
            arr2.pop(-1)
            arr2.pop(-1)
#print(arr2)
if arr2[-1] == arr2[-2]:
    arr2.pop(-1)
    arr2.pop(-1)
print(''.join(arr2))
'''
from collections import deque
s = deque()
rev = False
#print(s, s[0])
for i in input():
    if i == 'R':
        rev = not rev
    elif rev:
        if s and s[0] == i:
            s.popleft()
        else:
            s.appendleft(i)
    else:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
if rev:
    s = reversed(s)
print("".join(s))
