import sys
input = sys.stdin.readline
a = int(input())
z = []
for i in range(a):
    r = int(input())
    z.append(r)
z.sort()
l = 0
r = a // 2
count = 0
while (l < a // 2 and r < len(z)):
    if (z[l] * 2 <= z[r]):
        count += 1
        r += 1
        l += 1
    else:
        r += 1
print(len(z) - count)




