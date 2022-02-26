import math
# region fastio
import os
import sys
from io import BytesIO, IOBase

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


def dfs(tree, node, cat):
    n = len(tree)
    visited = [False]*(n)
    stk = [node]
    arr2 = [0]*(n)
    arr2[1] = cat[1]
    result = []
    while stk:
        v = stk[-1]
        if not visited[v]:
            visited[v] = True
            for u in tree[v]:
                if not visited[u]:
                    if arr2[v] > m:
                        arr2[u] = arr2[v]
                    elif cat[u] == 0:
                        arr2[u] = 0
                    else:
                        arr2[u] = arr2[v] + 1
                    stk.append(u)
                    #print(stk)
        else:
            if len(tree[v]) == 1 and v != 1:
                result += [arr2[v]]
            #print(stk)
            stk.pop()
    return result


N, m = list(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
tree = [[]for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)
#print(tree)
ans = dfs(tree, 1, arr)
print(len([ooo for ooo in ans if ooo <= m]))
#print(ans)