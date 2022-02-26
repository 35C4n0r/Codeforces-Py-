def dfs(u, cur):
    global ans
    vis[u] = True
    flag = True
    # print(vec[u], u)
    for x in vec[u]:
        v = x[0]
        c = x[1]
        if not vis[v]:
            dfs(v, cur + c)
            flag = False
    if flag:
        ans = max(cur, ans)
        # print(sna)


ans = 0
vec = [[]]
vis = []
i = 0
n = int(input())
while i < n:
    vec.append([])
    vis.append(False)
    i += 1
i = 1
while i < n:
    c = 1
    u, v = (int(x) for x in input().split())
    vec[u - 1].append((v - 1, c))
    vec[v - 1].append((u - 1, c))
    i += 1
# print(vec)
dfs(0, 1)
if ans == 1:
    print(n)
else:
    print(n - ans)