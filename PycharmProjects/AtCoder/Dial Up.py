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
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
fl = False
fll = False
ans = 0
if set(arr) == set(arr2):
    a = arr[0]
    b = arr[0]
    if 0 in arr:
        f0 = arr.index(0)
        fl = True
    if 1 in arr:
        fll = True
        f1 = arr.index(1)
    arr3 = list(reversed(arr))
    if fl:
        ff0 = arr3.index(0)
    if fll:
        ff1 = arr3.index(1)
    if fl:
        a0 = min(ff0, f0)
    if fll:
        a1 = min(f1, ff1)
    #print(a0, a1)
    for j in arr2:
        if j == 0:
            ans += a0 + 1
            if j != a:
                ans += 1
                a = j
        else:
            ans += a1 + 1
            if j != a:
                ans += 1
                a = j
        print(ans)
else:
    print(-1)
    exit()
print(ans)