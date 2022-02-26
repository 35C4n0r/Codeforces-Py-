n, k = list(map(int, input().split()))
hardness = sorted(list(map(int, input().split())))
print(hardness)
count = 0
j = 0
i = n-1
while j < i:
    if hardness[j] + hardness[i] < k:
        count += i - j
        j += 1
    else:
        i -= 1
print(count)





