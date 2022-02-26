from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
z = [4, 8, 15, 16, 23, 42]
arr2 = [0]*6
sit = {}
for l in range(6):
    sit[z[l]] = l
for k in arr:
    smh = sit[k]
    if arr2[smh-1] > 0 or smh == 0:
        arr2[smh] += 1
        if smh != 0:
            arr2[smh-1] -= 1
print(n - 6*arr2[5])
