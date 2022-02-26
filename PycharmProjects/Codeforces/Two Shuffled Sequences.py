n = int(input())
arr = list(map(int, input().split()))
arr3 = []
arr4 = []
arr2 = sorted(list(set(arr)))
for k in range(len(arr2)):
    arr3.append(arr.count(arr2[k]))
    if arr.count(arr2[k]) == 2:
        arr4.append(arr2[k])
if max(arr3) > 2:
    print("NO")
    exit()
print("YES")
print(len(arr4))
for t in (sorted(arr4)):
    print(t, end=" ")
print()
print(len(arr2))
for tt in (sorted(arr2, reverse=True)):
    print(tt, end=" ")