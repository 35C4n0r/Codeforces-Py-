# 1100
lp = []
np = []
b = 0
bb = 0
for _ in range(int(input())):
    z, n = list(map(int, input().split()))

    if z == abs(z):
        lp.append([z, n])
    else:
        np.append([z, n])
lp = sorted(lp)
np = sorted(np, reverse=True)
if len(lp) == len(np):
    for j in range(len(np)):
        b += np[j][1] + lp[j][1]
elif len(lp) > len(np):
    for j in range(len(np)):
        b += np[j][1]
        b += lp[j][1]
    b += lp[len(np)][1]

else:
    for j in range(len(lp)):
        b += lp[j][1]
        b += np[j][1]
    b += np[len(lp)][1]

print(b)