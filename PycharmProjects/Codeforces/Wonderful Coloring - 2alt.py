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
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    inf2 = {}
    inf = Counter(arr)
    ans = 0
    arr2 = [0]*n
    flag = 0
    for i in inf:
        inf2[i] = []
        if inf[i] >= k:
            ans += 1
        else:
            flag += inf[i]
            #print(flag, i)
            if flag >= k:
                #flag = 0
                ans += 1
                flag -= k
    print(ans)
    for b, bb in enumerate(arr):
        inf2[bb].append(b)
    print(inf2)
    flag3 = 0
    for v in range(ans):
        flag3 = 0
        for vv in range(ans):
            for c in inf2:
                while flag3 < vv:
                    arr2[inf2[c][v]] = v+1
                    flag3 += 1
    '''for v in inf2:
        if flag3 >= ans:
            break
        flag3 += 1
        flag2 = 0
        while flag2 < min(ans, len(inf2[v])):
            print(v, flag2)
            print(inf2[v][flag2])
            arr2[inf2[v][flag2]] = flag2+1
            flag2 += 1
    print(*arr2)'''
    print(*arr2)