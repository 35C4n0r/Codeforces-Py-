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


def dfs(i, j, ind, curr):
    #print(ind)
    if not vis[i][j]:
        arr2[i][j] = curr + 1
        vis[i][j] = True
        #print(ind)
        if i - 1 >= 0 and arr[i - 1][j] == alpha[ind+1]:
            #curr += 1
            dfs(i - 1, j, ind + 1, arr2[i][j])
        if i + 1 < h and arr[i + 1][j] == alpha[ind + 1]:
            #curr += 1
            dfs(i + 1, j, ind + 1, arr2[i][j])
        if j - 1 >= 0 and arr[i][j - 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i, j - 1, ind + 1, arr2[i][j])
        if j + 1 < w and arr[i][j + 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i, j + 1, ind + 1, arr2[i][j])
        if i + 1 < h and j + 1 < w and arr[i + 1][j + 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i + 1, j + 1, ind + 1, arr2[i][j])
        if i + 1 < h and j - 1 >= 0 and arr[i + 1][j - 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i + 1, j - 1, ind + 1, arr2[i][j])
        if i - 1 >= 0 and j + 1 < w and arr[i - 1][j + 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i - 1, j + 1, ind + 1, arr2[i][j])
        if i - 1 >= 0 and j - 1 >= 0 and arr[i - 1][j - 1] == alpha[ind + 1]:
            #curr += 1
            dfs(i - 1, j - 1, ind + 1, arr2[i][j])

    # print(local_var)


case = 0
while True:
    case += 1
    h, w = list(map(int, input().split()))
    if [h, w] == [0, 0]:
        break
    arr = []
    for _ in range(h):
        arr.append(list(input()))
    # print(arr)
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ%'
    alpha = list(al)
    #global ans
    ans = 0
    vis = [[False for o in range(w + 1)] for oo in range(h + 1)]

    arr2 = [[0 for ooo in range(w+1)] for oooo in range(h+1)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'A':
                curr = 0
                dfs(i, j, 0, curr)
    for i in range(h):
        ans = max(max(arr2[i]), ans)
    #print(arr2)
    print(f'Case {case}: {ans}')