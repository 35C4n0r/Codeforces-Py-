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
n, m = list(map(int, input().split()))
arr = {}
arr3 = [j for j in range(1, n+1)]
for ___ in range(m):
    a, b = list(map(int, input().split()))
    if a in arr:
        arr[a].append(b)
    else:
        arr[a] = [b]
    if b in arr:
        arr[b].append(a)
    else:
        arr[b] = [a]
q = int(input())
for __ in range(q):
    arr2 = list(map(int, input().split()))
    if arr2[0] == 3:
        for jj in list(arr):
            if min(arr[jj]) > jj:
                arr3.pop(jj-1)
                arr.pop(jj)
        print(len(arr3))
    else:
        no, aa, bb = arr2
        if no == 1:
            if aa in arr:
                arr[aa].append(bb)
            else:
                arr[aa] = [bb]
            if bb in arr:
                arr[bb].append(aa)
            else:
                arr[bb] = [aa]
        if no == 2:
            arr[aa].remove(bb)
            arr[bb].remove(aa)
