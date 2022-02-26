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
nn = int(input())
for _ in range(nn):
    space = input()
    k, n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    p1 = 0
    p2 = 0
    arr3 = []
    flag = True
    print(8)
    while len(arr3) != n+m:

    '''while len(arr3) != n + m:
        #print(p1, p2, arr[p1], arr2[p2])
        if p1 < n and arr[p1] == 0:
            p1 += 1
            k += 1
            arr3.append(0)
        elif p2 < m and arr2[p2] == 0 :
            k += 1
            p2 += 1
            arr3.append(0)
        elif p1 < n and arr[p1] > 0:
            if arr[p1] <= k:
                arr3.append(arr[p1])
                p1 += 1
            else:
                if arr2[p2] <= k:
                    arr3.append(arr2[p2])
                    p2 += 1

                else:
                    flag = False
                    break
        else:
            flag = False
            break
    arr3 = arr + arr2
    arr3.sort()
    flag = True
    for kk in arr3:
        if kk == 0:
            k += 1
        else:
            if k < kk:
                flag = False
                break'''
    '''if flag:
        print(*arr3)
    else:
        print(-1)'''
