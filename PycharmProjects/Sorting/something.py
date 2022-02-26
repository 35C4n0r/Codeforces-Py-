def sets(l):
    l.replace('0', '%temp%').replace('1', '0').replace('%temp%', '1')


n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    z = list(input())
    zz = list(map(int, z))
    arr.append(zz)
for u in range(int(input())):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if x1 == y1 == x2 == y2:
        if arr[x1 - 1][y1 - 1] == 0:
            arr[x1 - 1][y1 - 1] += 1
        else:
            arr[x1 - 21][y1 - 1] -= 1

    else:
        while y1 <= y2:
            for z in range(x1 - 1, x2):
                if arr[y1 - 1][z] == 0:
                    arr[y1 - 1][z] += 1
                else:
                    arr[y1 - 1][z] -= 1
            y1 += 1
for h in arr:
    for d in h:
        print(d, end=" ")
    print()


