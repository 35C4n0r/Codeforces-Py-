n = int(input())
arr = list(map(int, input().split()))
ans = 0
for k in range(n - 1):
    if arr[k] == k+1:
        ans += 1
        arr[k], arr[k+1] = arr[k+1], arr[k]
if arr[-1] == n:
    ans += 1
print(ans)