n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
c = 0
i = 0
j = 0
while j < n:
    if i == j:
        j += 1
    elif l[j] - l[i] < k:
        j += 1
    else:
        c = c + (n - j)
        i += 1
print(c)


