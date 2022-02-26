import sys
sys.setrecursionlimit(10**6)


def dfs(num):
    vis[num] = True
    if num in arr:
        for kk in arr[num]:
            if not vis[kk]:
                vis[kk] = True
                dfs(kk)


arr = {}
n, m = list(map(int, input().split()))
ans = []
vis = [False] * n
for _ in range(m):
    a, b = list(map(int, input().split()))
    if a - 1 in arr:
        arr[a - 1].append(b - 1)
    else:
        arr[a - 1] = [b - 1]
    if b - 1 in arr:
        arr[b - 1].append(a - 1)
    else:
        arr[b - 1] = [a - 1]

for b in range(n):
    if not vis[b]:
        ans.append(b)
        dfs(b)
print(len(ans) - 1)
for jj in range(len(ans) - 1):
    print(ans[jj] + 1, ans[jj+1] + 1)