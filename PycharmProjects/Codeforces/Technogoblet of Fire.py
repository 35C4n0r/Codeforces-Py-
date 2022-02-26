n, m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
ans = {}
count = 0
for z in range(n):
    if arr2[z] in ans:
        ans[arr2[z]].append([arr[z], z+1])
    else:
        ans[arr2[z]] = [[arr[z], z+1]]
#print(sna)
for zz in arr3:
    key = arr2[zz-1]
    power = arr[zz-1]
    ans[key].sort(reverse=True)
    res = ans[key]
    if res[0] != [power, zz]:
        count += 1
        ans[key].remove([power, zz])
print(count)