from collections import *
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
    ans = 0
    if arr[0] != 'R':
        ans += 1
        arr[0] = "R"
    if arr[-1] != "R":
        ans += 1
        arr[-1] = "R"
    if 'W' not in arr:
        ans += 1
        print(ans)
    else:
        pointer_front = 0
        pointer_back = 0
        for k in range(n):
            if arr[k] == 'W':
                pointer_front = k
                break
        for k in range(n-1, -1, -1):
            if arr[k] == 'W':
                pointer_back = k+1
                break
        arr3 = arr[pointer_front:pointer_back]
        arr2 = Counter(arr3)
        #print(arr2, arr3, pointer_back,pointer_front)
        if 'R' in arr2:
            if arr2['R'] > arr2['W'] - 1:
                ans += arr2['W'] - 1
            else:
                ans += arr2['R']
        print(ans)