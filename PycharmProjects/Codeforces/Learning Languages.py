def dfs(u):
    global ans
    vis[u] = True
    for x in vec[u]:
        if not vis[x]:
            dfs(x)


n, m = list(map(int, input().split()))
i = 0
vec = []
vis = [False]*m
print(vis)
for _ in range(m):
    vec.append([])
for _ in range(n):
    lis = list(map(int, input().split()))
    f = lis[0]
    if f != 0:
        lis.pop(0)
        for kkk in lis:
            vec[kkk - 1].append(_)
            #vec[kkk - 1].append(_)
dfs(0)
print(vec)
print(vec[0])

