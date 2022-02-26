n, k = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
count = 0
i = 0
j = n - 1
while j >= i:
    if i == j:
        count += 1
        break
    elif arr[j] + arr[i] <= k:
        count += 1
        i += 1
        j -= 1
    else:
        count += 1
        j -= 1

print(count)