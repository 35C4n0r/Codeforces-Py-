# 1100
arr2 = []
for _ in range(int(input())):
    n = input()
    arr2.append(n)
arr2 = sorted(arr2, key=len)
for k in range(len(arr2) - 1):
    if arr2[k] not in arr2[k + 1]:
        print("NO")
        exit()
print("YES")
for kk in arr2:
    print(kk)