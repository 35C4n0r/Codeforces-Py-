import math
def dfs(u, cur):
    global ans
    vis[u] = True
    #print(vis)
    flag = True
    #print(vec[u], u)
    for x in vec[u]:
        #print(x)
        z = x
        #print(u, gg)
        if not vis[z]:
            if (u, z) in arr100:
                #print(u, gg, 100000)
                cur += arr100[u, z]
            dfs(z, cur)
            flag = False
    if flag:
        vis2 = vis.copy()
        vis2.pop(0)
        #print(vis2, [True]*(jkj-1))
        #print(u, 1, 99999999999)
        if vis2 == [True]*(n):
            #print("YEs")
            if (u, 1) in arr100:
                cur += arr100[u, 1]
        ans = min(cur, ans)
        #print(sna)


ans = math.inf
ass = 0
vec = []
vis = []
i = 0
arr100 = {}
n = int(input())
while i < n + 1:
    vec.append([])
    vis.append(False)
    i += 1
i = 1
while i <= n:
    u, v, c = (int(x) for x in input().split(' '))
    ass += c
    vec[u].append(v)
    vec[v].append(u)
    arr100[u, v] = c
    i += 1
#print(vec)

dfs(1, 0)
#print(ass - sna)
#print(vec)
print(min(ass - ans, ans))