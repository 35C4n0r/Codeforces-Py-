'''jkj = int(input())
friends = {}
cat = {}
cost = 0
count = 0
arr3 = []
arr4 = [0]
for _ in range(jkj - 1):
    lis = list(map(int, input().split()))
    arr = lis[0]
    pre_n_post = lis[1]
    c = lis[2]
    cat[max(arr, pre_n_post), min(arr, pre_n_post)] = c
    if arr in friends:
        friends[arr].append(pre_n_post)
    else:
        friends[arr] = [pre_n_post]
    if pre_n_post in friends:
        friends[pre_n_post].append(arr)
    else:
        friends[pre_n_post] = [arr]
print(friends)
print(cat)
xxx = 0
while count <= jkj:
    arr1000 = []
    long = False
    index = 0
    arr3 = friends[xxx]
    #print(arr3)
    for node in arr3:
        if node not in arr4:
            arr1000.append(cat[max(node, xxx), min(node, xxx)])
            long = True
    if not long:
        print(cost, 10000)
        exit()
    use = max(arr1000)
    count += 1
    print(arr3)
    #print(use)
    cost += use
    arr4.append(xxx)
    xxx = arr3[arr1000.index(use)]
print(cost)
print(friends)'''


def dfs(u, cur):
    global ans
    vis[u] = True
    flag = True
    #print(vec[u], u)
    for x in vec[u]:
        v = x[0]
        c = x[1]
        if not vis[v]:
            dfs(v, cur+c)
            flag = False
    if flag:
        ans = max(cur, ans)
        #print(sna)


ans = 0
vec = []
vis = []
i = 0
n = int(input())
while i < n:
    vec.append([])
    vis.append(False)
    i += 1
i = 1
while i < n:
    u, v, c = (int(x) for x in input().split(' '))
    vec[u].append((v, c))
    vec[v].append((u, c))
    i += 1
#print(vec)
dfs(0, 0)
print(ans)
