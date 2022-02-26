import math
# region fastio
import os
import sys
from io import BytesIO, IOBase
sys.setrecursionlimit(10**6)
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion
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

for k in range(n):
    if not vis[k]:
        ans.append(k)
        dfs(k)
print(len(ans) - 1)
for jj in range(len(ans) - 1):
    print(ans[jj] + 1, ans[jj + 1] + 1)
'''arr = {}
n, m = list(map(int, input().split()))
for i in range(m):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
    else:
        arr[a] = [b]
    if b in arr:
        arr[b].append(a)
    else:
        arr[b] = [a]

tt = [False]*(n+1)


def dfs(x):
    if '''