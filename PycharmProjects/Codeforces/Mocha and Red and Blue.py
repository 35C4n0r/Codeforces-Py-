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
for _ in range(int(input())):
    n = int(input())
    s = input()
    arr = list(s)
    print(z)
    arr2 = arr.copy()
    if arr[0] == '?':
        arr2[0] = 'B'
    for k in range(1, n):
        if arr2[k] == '?':
            if arr2[k-1] == 'B':
                arr2[k] = 'R'
            else:
                arr2[k] = 'B'
    arr3 = arr.copy()
    if arr[0] == '?':
        arr3[0] = 'R'
    for k in range(1, n):
        if arr3[k] == '?':
            if arr3[k - 1] == 'B':
                arr3[k] = 'R'
            else:
                arr3[k] = 'B'
    x = 0
    y = 0
    for kk in range(1, n):
        if arr2[kk] == arr2[kk-1]:
            x += 1
        if arr3[kk] == arr3[kk-1]:
            y += 1
    if x > y:
        print(''.join(arr3))
    else:
        print(''.join(arr2))