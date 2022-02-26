n = int(input())
arr = list(input())
arr2 = list(input())
ans = 0
for k in range(n):
    if arr[k] != arr2[k]:
        if k != n-1:
            #print(k)
            if arr[k+1] != arr2[k+1] and arr[k] == arr2[k+1] and arr[k+1] == arr2[k]:
                ans += 1
                arr[k], arr[k+1] = arr[k+1], arr[k]
            else:
                ans += 1
                arr[k] = arr2[k]
if arr[-1] != arr2[-1]:
    ans += 1
print(ans)
