"""
ID: jay20ma1
LANG: PYTHON3
TASK: dualpal
"""
input = open('paint.in', 'r').readline
fout = open('paint.out', 'w')
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
fout.write(str(((b-a) + (d-c)) - (max(0, min(b, d)-max(a, c)))))
fout.close()