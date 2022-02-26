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


def one():
    for i in range(0, 2*n, 2):
        arr[i],arr[i+1] = arr[i+1], arr[i]


def two():
    for i in range(0, n):
        arr[i], arr[n+i] = arr[n+i], arr[i]
        #print(i, n+i)


n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr)
ans = math.inf
if n % 2 == 0:
    for i in range(4):
        if i%2 == 0:
            one()
            if arr2 == arr:
                print((i+1)%4)
                exit()
        else:
            two()
            if arr == arr2:
                print((i+1)%4)
                exit()
else:
    for i in range(2*n):
        if i%2 == 0:
            two()
            if arr2 == arr:
                ans = (i+1)%(2*n)
                break
        else:
            one()
            if arr == arr2:
                ans = (i+1)%(2*n)
                break
    for i in range(2*n):
        if i%2 == 0:
            one()
            if arr2 == arr:
                ans = min(ans,(i+1)%(2*n))
                exit()
        else:
            two()
            if arr == arr2:
                ans = min(ans,(i+1)%(2*n))
                break
    if ans != math.inf:
        print(ans)
        exit()
print(-1)