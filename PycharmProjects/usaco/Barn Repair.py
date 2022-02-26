"""
ID: jay20ma1
LANG: PYTHON3
TASK: barn1
"""
fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')
m, s, c = list(map(int, fin.readline().split()))
arr2 = []
arr3 = []
count = 0
for _ in range(c):
    arr2.append(int(fin.readline()))
arr2.sort()
#print(arr2)
for k in range(c-1):
    arr3.append(arr2[k+1]-arr2[k])
#print(arr3)
z = min(c - 1, m - 1)
while z != 0 and set(arr3) != {1}:
    arr3.remove(max(arr3))
    #print(arr3)
    z -= 1
    count += 1
fout.write(f'{sum(arr3) + count + 1}')
fout.write('\n')
fout.close()