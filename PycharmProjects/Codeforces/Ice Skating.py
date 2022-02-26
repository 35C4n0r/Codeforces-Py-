arr = []
xco = {}
yco = {}
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x in xco:
        xco[x].append([x, y])
    else:
        xco[x] = [[x, y]]
    if y in yco:
        yco[y].append([x, y])
    else:
        yco[y] = [[x, y]]
    arr.append([x, y])
print(xco)
print(yco)