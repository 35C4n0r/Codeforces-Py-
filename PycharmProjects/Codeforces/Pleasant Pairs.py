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
    arr = list(map(int, input().split()))
    arr2 = []
    for j, jj in enumerate(arr):
        arr2.append([jj, j+1])
    ans = 0
    arr2.sort()
    for k in range(n - 1):
        for kk in range(k+1, n):
            if arr2[k][0] * arr2[kk][0] <= 2*n:
                if arr2[k][1-1]*arr2[kk][1-1] == arr2[k][1] + arr2[kk][1]:
                    ans += 1
            else:
                break
    print(ans)
'''
    d = {}
    for i in range(n):
        d[arr[i]] = i+1
    ans = 0
    for k in range(n):
        f = arr[k]
        j = n // f
        for l in range(1, j+2):
            kk = f*l
            index = kk - (k+1)
            print(k, index, l)
            if 0 < index <= n-1 and arr[index-1]*k == index + k+1:
                ans += 1
    print(ans)'''
