def shit(tea, kk):
    



n, m = list(map(int, input().split()))
arr = {}
arrm = {}
for _ in range(1, n+1):
    arr[_] = []
    arrm[_] = 0
for _ in range(m):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
    if b in arr:
        arr[b].append(a)
print(arr)
q = int(input())
for _ in range(q):
    v, d, c = list(map(int, input().split()))
    tea = arr[v]
    tt = [0] * (n+1)
    for kk in range(1, len(tea)+1):
        #tt[kk] += 1
        if d > 0:
            #arrm[tea[kk]] = c
            shit(tea, kk)
print(arrm)