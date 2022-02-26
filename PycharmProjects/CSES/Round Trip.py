def dfs(num, count, arr):
    global ans
    if count > 2:
        for kk in vec[num]:
            if vis[kk]:
                print(*arr)
                exit()
    for kkk in vec[num]:
        vis[kkk] = True
        arr.append(kkk)
        count += 1
        dfs(kkk, count, arr)


ans = 0
n, k = list(map(int, input().split()))
vec = []
vis = []
for _ in range(k):
    vec.append([])
    vis.append(False)
for _ in range(k):
    a, b = list(map(int, input().split()))
    vec[a].append(b)
    vec[b].append(a)
print(vec)
dfs(1, 0, [])
print("IMPOSSIBLE")