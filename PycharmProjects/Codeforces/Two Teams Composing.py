fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
for _ in range(int(fin.readline())):
    n = int(fin.readline())
    arr = list(map(int, fin.readline().strip('\n').split()))
    z = len(arr)
    zz = len(list(set(arr)))
    count = 1
    if z == 1:
        fout.write('0')
        fout.write('\n')
    elif z == zz:
        fout.write('1')
        fout.write('\n')
    else:
        for k in set(arr):
            count = max(count, arr.count(k))
        fout.write(str(max(min(count-1, zz), min(count, zz-1))))
        fout.write('\n')
fout.close()



