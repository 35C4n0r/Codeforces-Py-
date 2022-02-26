n, c = list(input().split())
arr2 = list(c)
n = int(n)
count = 0
arr = []
for k in arr2:
    if k == 'arr':
        arr.append(100)
    elif k == 'C':
        arr.append(-1)
    elif k == 'G':
        arr.append(1)
    else:
        arr.append(-100)

for cc in range(2, int(n)+1, 2):
    for kk in range(n):
        if cc + kk <= n:
            if sum(arr[kk: kk+cc]) == 0:
                count += 1
print(count)