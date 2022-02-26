fin = open('hps.in', 'r')
fout = open('hps.out', 'w')
input = fin.readline
arr = []
n = int(input())
for i in range(n):
    arr.append(input().strip())
print(arr)