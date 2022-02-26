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


def is_palindrome(arr):
    l = 0
    flag = True
    r = len(arr)-1
    while l < r:
        if arr[l] != arr[r]:
            flag = False
            break
        l += 1
        r -= 1
    if flag:
        return -1
    else:
        return [l, r]


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    j = is_palindrome(arr)
    if j == -1:
        print("YES")
        continue
    a, b = j
    '''s = ''
    for i in arr:
        s += str(i)'''
    '''arr2 = s
    arr3 = s'''
    '''arr2 = arr.copy()
    arr3 = arr.copy()'''
    '''aa = arr2.count(arr[arr])
    bb = arr3.count(arr[b])'''
    arr4 = []
    arr5 = []
    for i in range(n):
        if arr[i] != arr[a]:
            arr4.append(arr[i])
        if arr[i] != arr[b]:
            arr5.append(arr[i])
    '''for jj in range(len(arr4)):
        arr2.pop(arr4[jj] - jj)
    for jj in range(len(arr5)):
        arr3.pop(arr5[jj] - jj)'''
    '''while aa > 0:
        aa -= 1
        arr2.remove(arr[arr])
    while bb > 0:
        bb -= 1
        arr3.remove(arr[b])'''
    '''arr2 = arr2.replace(str(arr[arr]), "")
    arr3 = arr3.replace(str(arr[b]), "")'''
    #print(arr2, arr3)
    #print(arr4, arr5)
    if is_palindrome(arr4) == -1 or is_palindrome(arr5) == -1:
        print("YES")
    else:
        print("NO")