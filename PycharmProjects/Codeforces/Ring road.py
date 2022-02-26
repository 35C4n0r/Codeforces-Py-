'''lis = {}
arr1000 = {}
cost = 0
cost2 = 0
jkj = int(input())
arr3 = [False]*jkj
for _ in range(jkj):
    arr, pre_n_post, c = list(map(int, input().split()))
    cost2 += c
    if arr in lis:
        lis[arr].append(pre_n_post)
    else:
        lis[arr] = [pre_n_post]
    if pre_n_post in lis:
        lis[pre_n_post].append(arr)
    else:
        lis[pre_n_post] = [arr]
    arr1000[arr, pre_n_post] = c
print(lis)
print(arr1000)
count = 0
arr1000 = []
for k in lis:
    if len(lis[k]) > 1:
        for kk in lis[k]:
            if kk not in lis:
                #print(kk)
                cost += arr1000[k, kk]
print(min(cost, cost2-cost))'''


'''jkj = int(input())
cnt1 = [0] * (jkj + 1)
cnt2 = [0] * (jkj + 1)
aaaa = 0
s1 = 0
d1 = {}
d2 = {}
for _ in range(jkj):
    smh, smh2, cc = list(map(int, input().split()))
    print(d1)
    print(d2)
    if (smh in d1) or (smh2 in d2):
        smh, smh2 = smh2, smh
        s1 += cc
    d1[smh] = 1
    d2[smh2] = 1
    aaaa += cc

print(min(s1, aaaa - s1))'''

'''5 
1 4 1
4 2 1
2 3 1
5 3 1
1 5 3

6
1 6 1
1 5 1
5 3 1
2 3 1
2 4 1
4 6 1'''
'''lis = {}
arr1000 = {}
cost = 0
cost2 = 0
jkj = int(input())
arr1000 = [0]*jkj
for _ in range(jkj):
    arr, pre_n_post, c = list(map(int, input().split()))
    arr1000[pre_n_post - 1] += 1
    cost2 += c
    if arr in lis:
        lis[arr].append(pre_n_post)
    else:
        lis[arr] = [pre_n_post]
    arr1000[arr, pre_n_post] = c
print(lis)
print(arr1000)
count = 0
for k in lis:
    if len(lis[k]) > 1:
        for kk in lis[k]:
            if kk not in lis:
                print(kk)
                cost += arr1000[k, kk]
print(min(cost, cost2-cost))'''
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