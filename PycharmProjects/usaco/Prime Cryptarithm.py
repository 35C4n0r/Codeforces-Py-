"""
ID: jay20ma1
LANG: PYTHON3
TASK: crypt1
"""
'''import itertools
fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')
n = int(fin.readline())
arr = list(map(int, fin.readline().split()))
arr.sort()
print(arr)
for k in itertools.permutations(arr, 3):
    for kk in itertools.combinations_with_replacement(arr, 2):
        print(kk, k)'''
fin = open('crypt1.in', 'r')
n = int(fin.readline().strip())
nList = [int(e) for e in fin.readline().strip().split(" ")]


def isMember(p):
    isMember = True
    for e in p:
        if nList.count(int(e)) == 0:
            isMember = False
            break
    return isMember


cnt = 0
for a in nList:
    for b in nList:
        for c in nList:
            for d in nList:
                for e in nList:
                    isValid = True
                    pList = []
                    abc = a * 100 + b * 10 + c

                    for i, de in enumerate([e, d]):
                        p = str(abc * de)
                        if len(p) > 3:
                            isValid = False
                            break
                        else:
                            if not isMember(p):
                                isValid = False
                                break
                        if isValid:
                            pList.append(p)
                        else:
                            break
                    if not isValid:
                        continue
                    result = int("0" + pList[0]) + int(pList[1] + "0")
                    if isMember(str(result)):
                        cnt += 1

with open('crypt1.out', 'w') as fout:
    fout.write(f"{cnt}\n")

