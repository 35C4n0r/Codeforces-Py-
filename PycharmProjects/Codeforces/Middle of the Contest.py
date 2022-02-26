n = input().replace(":", " ")
nn = input().replace(":", " ")
arr1 = list(map(int, n.split()))
arr2 = list(map(int, nn.split()))
arr3 = ["0"]
arr4 = ["0"]

z = arr1[0]+arr2[0]
if z == 0:
    z = 24
z //= 2
z = str(z)
if len(z) == 1:
    arr3.insert(1, z)
    z = "".join(arr3)

zz = arr1[1] + arr2[1]
if zz == 00:
    zz = 60
if arr1[1] == 0 and arr2[1] != 0:
    zz = 60 + arr2[1]
elif arr1[1] != 0 and arr2[1] == 0:
    zz = arr1[1] + 60
zz //= 2
zz = str(zz)
if len(zz) == 1:
    arr4.insert(1, zz)
    zz = "".join(arr4)
print(f"{z}:{zz}")