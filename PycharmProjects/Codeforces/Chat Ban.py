import decimal
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
decimal.getcontext().prec = 100
for _ in range(int(input())):
    k, x = list(map(int, input().split()))
    '''if _ == 81 and (k > 99999 or x > 99999):
        print(x, k)'''
    s = (math.ceil(((decimal.Decimal(x * 8 + 1).sqrt() - 1) / 2)))
    #print(416881849**2)
    #o = 1 + (8*x)
    #ooo = -1 + float(o**(1/2))
    #oooo = ooo / 2
    #print(o, ooo, oooo)
    if s <= k:
        print(math.ceil(((decimal.Decimal(x * 8 + 1).sqrt() - 1) / 2)))
        print(decimal.Decimal(x * 8 + 1).sqrt())
    else:
        x -= math.ceil(decimal.Decimal(((k-1)*(k)) / 2))
        #print(x)
        c0 = (2*k) + 1
        c1 = ((2*k) + 1) ** 2
        c3 = 8*x
        if c3 > c1:
            print(k+k-1)
            continue

        c4 = decimal.Decimal(c1 - c3).sqrt()
        c5 = decimal.Decimal((c0 - c4) / 2)
        #print(x, c1, c3, c5)
        ans = (k - 1) + math.ceil(c5)
        print(ans)
'''for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    s = (n*(n+1)) // 2
    
    if n**2 <= m:
        print(n+n-1)
    elif s >= m:
        print(math.ceil(((decimal.Decimal(m * 8 + 1).sqrt() - 1) / 2)))
    else:
1
430302156 21723809503207353'''

