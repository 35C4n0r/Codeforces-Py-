fin = open('word.in', 'r')
fout = open('word.out', 'w')
n, k = list(map(int, fin.readline().split()))
s = fin.readline()
sent = list(map(str, s.split()))
count = 0
for kk in sent:

    if count + len(kk) > k:
        fout.write('\n' + kk + ' ')
        count = len(kk)
    else:
        fout.write(kk)
        fout.write(' ')
        count += len(kk)
#fout.write('\n')
fout.close()


