n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = arr.copy()
arr2.sort()
xxx = k
sem = 0
idk = {}
for k in range(n):
    idk[arr[k]] = k
for k in arr2:
    smh = idk[k]
    sem += abs(smh + 1 - xxx)
    xxx = smh + 1
print(sem)