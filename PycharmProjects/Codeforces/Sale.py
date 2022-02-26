n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for k in range(k):
    if arr[k] < 0:
        ans += abs(arr[k])
    else:
        print(ans)
        exit()
print(ans)