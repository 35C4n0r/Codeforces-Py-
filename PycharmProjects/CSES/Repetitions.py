arr = list(input())
ans, temp = 1, 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 1
ans = max(ans, temp)
print(ans)