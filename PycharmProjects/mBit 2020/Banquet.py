n = int(input())
arr = list(map(int, input().split()))
ans = 0
pointer = 0
for k in range(n):
    for kk in range(arr[k]):
        ans += abs(k - pointer)
        pointer += 1
print(ans)