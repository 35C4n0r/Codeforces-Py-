import sys
sys.setrecursionlimit(1500000)
input = sys.stdin.readline
def dfs(k):
    if arr2[k] == 1:
        return
    arr2[k] = 1
    if k in arr:
        for kk in arr[k]:
            dfs(kk)
    else:
        return
arr = {}
n, m = list(map(int, input().split()))
if m == 0:
    print(n)
    exit()
for i in range(m):
    a, b = list(map(int, input().split()))
    if a-1 in arr:
        arr[a-1].append(b-1)
    else:
        arr[a-1] = [b-1]
ans = 0
for k in range(n):
    arr2 = [0]*n
    dfs(k)
    ans += sum(arr2)
print(ans)