fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
arr = list(map(int, fin.readline().strip().split()))
arr3 = []
arr2 = set(arr)
for k in arr2:
    smh = arr.count(k)
    if smh % 2 != 0:
        fout.write('-1')
        exit()
    else:
        for _ in range(smh):
            arr3.append(arr.index(k) + 1)
            arr.remove(k)
for kkk in range(0, n - 1, 2):
    fout.write(f"{arr3[kkk]} {arr3[kkk + 1]}")
fout.close()
