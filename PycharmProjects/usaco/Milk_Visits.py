"""
ID: jay20ma1
LANG: PYTHON3
TASK: milkvisits
"""
fin = open('milkvisits.in', 'r')
fout = open('milkvisits.out', 'w')
n, m = list(map(int, fin.readline().split()))
arr = list(fin.readline())
#graph = {}
graph = [[] for __ in range(n+1)]


'''def dfs(vis, s, e, c):
    print(s, e, c)
    vis[s] = True
    if arr[s - 1] == c:
        return True
    for v in graph[s]:
        print(v)
        if v == e:
            return False
        if not vis[v - 1]:
            if dfs(vis, v, e, c):
                return True
    return False'''


for _ in range(n-1):
    a, b = list(map(int, fin.readline().split()))
    graph[a].append(b)
    '''if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]'''
ans = ''
for _ in range(m):
    a, b, c = fin.readline().split()
    aa = int(a)
    bb = int(b)
    vis = [False]*(n+1)
