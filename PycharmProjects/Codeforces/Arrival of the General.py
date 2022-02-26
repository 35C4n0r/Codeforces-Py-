n = int(input())
arr = list(map(int, input().split()))
z = arr.index(max(arr))
zz = arr.index(min(arr))
#print(zz,  gg)
if zz < z:
    print(abs(z) + abs(n - 1 - zz) - 2)
else:
    print(abs(z) + abs(n - zz - 1))