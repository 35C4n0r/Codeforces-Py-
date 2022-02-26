import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    visited[x][y] = True
    b, w = 0, 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        print(nx, ny, visited, [x, y], i)
        if 0 <= nx < H and 0 <= ny < W and (not visited[nx][ny]) and S[x][y] != S[nx][ny]:
            print(nx, ny, visited, [x, y], 1234567890)
            tmp_b, tmp_w = dfs(nx, ny)
            b += tmp_b
            w += tmp_w
    if S[x][y] == '#':
        return [b+1, w]
    else:
        return [b, w+1]


H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * W for _ in range(H)]
res = 0
for i in range(H):
    for j in range(W):
        if not visited[i][j]:
            cnt_b, cnt_w = dfs(i, j)
            res += cnt_b * cnt_w

print(res)