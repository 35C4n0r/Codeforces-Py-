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
n = int(input())
arr = list(map(int, input().split()))
dp = [[-math.inf for _ in range(n+1)] for __ in range(n+1)]
#dp2 = [[0 for _ in range(n+1)] for __ in range(n+1)]
ans = 0
dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, i+1):
        if dp[i-1][j-1] + arr[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j])
            ans = max(ans, j)
        elif dp[i-1][j] != -math.inf:
            dp[i][j] = dp[i-1][j]
print(ans)
print(dp)
'''for _ in range(int(input())):
    s = input()
    c1 = 0
    c2 = 0
    if "ab" in s:
        c1 += s.count("ab")
    if "ba" in s:
        c2 += s.count("ba")
    if c1 == c2:
        print(s)
        continue
    else:
        arr = list(s)
        arr2 = list(s)[::-1]
        if c1 > c2:
            z = s.index("aa")
            arr[z] = "b"
            print("".join(arr))
        else:
            z = s[::-1].index("bb")
            print(s[::-1])
            arr2[z] = "b"
            print(arr2)
            print("".join(arr2[::-1]))'''

'''try:
    s = input("Enter the expression you wat to simplify: ")
    print(eval(s))
except:
    print("Give Expression cannot be Evaluated")

s = int(input("Enter distance in Kms: "))
print(s * (0.621))'''

'''import numpy
n, m = list(map(int, input("Enter Dimensions of matrixes: ").split()))
matrix1 = []
print("Input Values for matrix1")
for i in range(n):
    matrix1.append(list(map(int, input().split())))
matrix2 = []
print("Input Values for matrix2")
for i in range(n):
    matrix2.append(list(map(int, input().split())))
matrix2 = numpy.array(matrix2)
matrix1 = numpy.array(matrix1)
ss = numpy.add(matrix1, matrix2)
for k in ss:
    for j in k:
        print(j, end=' ')
    print()'''

'''n, m = list(map(int, input("Enter Dimensions of matrixes: ").split()))
matrix1 = []
print("Input Values for matrix1")
for i in range(n):
    matrix1.append(list(map(int, input().split())))
matrix2 = []
print("Input Values for matrix2")
for i in range(n):
    matrix2.append(list(map(int, input().split())))

for k, kk in zip(matrix1, matrix2):
    for j, jj in zip(k, kk):
        print(j + jj, end=' ')
    print()'''