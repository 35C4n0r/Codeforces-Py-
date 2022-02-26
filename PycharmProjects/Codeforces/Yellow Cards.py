a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
man = 0
z = (k1 - 1) * a1 + (k2 - 1) * a2
if n <= z:
    men = 0
else:
    rem = n - z
    men = rem
if k1 < k2:
    zz = k2*a2
    if zz >= n:
        man +=