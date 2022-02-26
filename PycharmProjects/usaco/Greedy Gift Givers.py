"""
ID: jay20ma1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

n = int(fin.readline())
name = []
name2 = []
account = [0] * n
for i in range(n):
    name.append(fin.readline().strip("\n"))

for i in range(n):
    zzz = fin.readline().strip("\n")
    z = name.index(zzz)
    giving, number = list(map(int, fin.readline().split()))
    if giving == 0 and number != 0:
        for _ in range(number):
            m_n_useless = fin.readline()
        pass
    elif number == 0 or (giving == 0 and number == 0):
        pass
    else:
        account[z] -= giving - (giving % number)
        for _ in range(number):
            receiver = fin.readline().strip('\n')
            y = name.index(receiver)
            account[y] += giving // number

'''for bb in range(len(name)):
    name[bb] = name[bb].strip('\n')'''

for (a, b) in zip(name, account):
    fout.write(f"{a} {b}")
    fout.write('\n')
fout.close()
