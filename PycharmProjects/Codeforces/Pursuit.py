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
    arr2 = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr2.sort(reverse=True)
    pre_init = n - (n//4)
    s1 = sum(arr[:pre_init])
    s2 = sum(arr2[:pre_init])
    ans = 0
    while s2 > s1:
        ans += 1
        n += 1
        init = n - (n // 4)
        #print(pre_init, init, s1, s2, arr, n, "UwU")
        if pre_init == init:
            arr.insert(0, 100)
            s1 -= arr[init]
            s1 += 100
        else:
            if len(arr2) >= init:
                s2 += arr2[init-1]
            arr.insert(0, 100)
            s1 += 100
            pre_init = init
        #print(pre_init, init, s1, s2, arr, n)
    print(ans)