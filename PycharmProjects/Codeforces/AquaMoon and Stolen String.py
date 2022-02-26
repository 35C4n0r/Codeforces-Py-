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
    n, m = list(map(int, input().split()))
    arr = []
    arr2 = []
    for i in range(n):
        arr.append(list(input()))
    for ii in range(n-1):
        arr2.append(list(input()))
    k = 0
    #kk = 0
    while k < n // 2:
        for kk in arr2:
            flag = 0
            flag2 = True
            arr5 = arr[k].copy()
            arr6 = kk.copy()
            arr7 = arr[k].copy()
            arr8 = kk.copy()
            for j in range(m):
                if arr[k][j] != kk[j]:
                    flag += 1
                    arr5[j], arr6[j] = arr6[j], arr5[j]
                else:
                    arr7[j], arr8[j] = arr8[j], arr7[j]
                if flag > m:
                    flag2 = False
                    break

            if flag2:
                print(arr5, arr6, arr7, arr8)
                k -= 1
                #arr.remove(arr5)
                arr.remove(arr6)
                #arr2.remove(arr7)
                arr2.remove(arr8)
                break

        k += 1
    print(arr)