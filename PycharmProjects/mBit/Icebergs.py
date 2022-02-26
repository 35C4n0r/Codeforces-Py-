import math
n = int(input())
arr = []
wonder = {}
for _ in range(n):
    lmao = list(map(int, input().split()))
    arr.append(lmao)
    wonder[lmao[0], lmao[1]] = _
arr2 = arr.copy()
mark = 0
while len(arr) > 1:
    lol = math.inf
    index = 0
    cod = arr[mark]
    x1 = cod[0]
    y1 = cod[1]
    for kk in range(0, len(arr)):
        if kk != mark:
            cod2 = arr[kk]
            x2 = cod2[0]
            y2 = cod2[1]
            dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            #print(cod, cod2, dist)
            if dist < lol:
                index = kk
                lol = dist
    arr.pop(index)
    damn_me = arr.index(cod)
    mark = damn_me + 1
    if damn_me == len(arr) - 1:
        mark = 0
    #print(arr, mark, index)
print(wonder[arr[0][0], arr[0][1]] + 1)
'''10
4 2
-1 1
2 -1
2 5
6 10
10 10
20 20
30 30
0 3
40 40'''
