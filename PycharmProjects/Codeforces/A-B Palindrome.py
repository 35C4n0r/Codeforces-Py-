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
    a, b = list(map(int, input().split()))
    arr = list(input())
    info = Counter(arr)
    n = a+b
    flag = True
    #print(info)
    for k in range(n // 2):
        #print(k, n-k-1)
        if arr[k] != '?':
            if arr[k] == '1':
                if arr[n-k-1] == "?":
                    info['?'] -= 1
                    arr[n-k-1] = '1'

                elif arr[n-k-1] == "0":
                    flag = False
                    break
            if arr[k] == "0":
                if arr[n-k-1] == "?":
                    arr[n-k-1] = '0'
                    info['?'] -= 1

                elif arr[n-k-1] == "1":
                    flag = False
                    break
        if arr[n-k-1] != '?':
            if arr[n-k-1] == "1":

                if arr[k] == "?":
                    info['?'] -= 1
                    arr[k] = "1"

                elif arr[k] == "0":
                    flag = False
                    break
            if arr[n-k-1] == '0':
                if arr[k] == "?":
                    info['?'] -= 1
                    arr[k] = "0"

                elif arr[k] == "1":
                    flag = False
                    break
    #print(arr)
    info2 = Counter(arr)
    a -= info2["0"]
    b -= info2["1"]
    if a < 0 or b < 0:
        flag = False
    if flag:
        if (info['?'] % 2 == 0) or (info['?'] % 2 == 1 and arr[n//2] != "?"):
            #print(arr, b, info['?'])
            if a % 2 == 0 and b % 2 == 0:
                for j in range(n//2):
                    if arr[j] == "?":
                        if a > 0:
                            arr[j] = "0"
                            arr[n-j-1] = "0"
                            a -= 2
                        elif b > 0:
                            arr[j] = "1"
                            arr[n-j-1] = "1"
                            b -= 2
                        if a == 0 and b == 0:
                            break
            else:
                flag = False
                print(-1)
        else:
            if a % 2 != 0 or b % 2 != 0:
                if a % 2 == 1:
                    arr[n//2] = "0"
                    a -= 1
                else:
                    arr[n//2] = "1"
                    b -= 1
                for j in range(n//2):
                    if arr[j] == "?":
                        if a > 0:
                            arr[j] = "0"
                            arr[n-j-1] = "0"
                            a -= 2
                        elif b > 0:
                            arr[j] = "1"
                            arr[n-j-1] = "1"
                            b -= 2
                        if a == 0 and b == 0:
                            break
            else:
                flag = False
                print(-1)
    else:
        print(-1)
    if flag:
       print(''.join(arr))