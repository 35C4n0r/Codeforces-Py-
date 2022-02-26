"""
ID: jay20ma1
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')


def reVal(num):
    if num >= 0 and num <= 9:
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))


def fromDeci(res, base, inputNum):
    index = 0
    while inputNum > 0:
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)
    res = res[::-1]
    return res


n, s = list(map(int, fin.readline().split()))
count = 0
while count < n:
    every = 0
    s += 1
    for kk in range(2, 11):
        r = str(fromDeci("", kk, s))
        #print(r, kk, s, count, every)
        if len(r) == 1:
            every += 1
            if every == 2:
                count += 1
                fout.write(f"{s}")
                fout.write('\n')
                break
        else:
            if len(r) % 2 != 0:
                if list(r[: len(r) // 2]) == list(reversed(r[(len(r) // 2) + 1:])):
                    every += 1
                    if every == 2:
                        count += 1
                        fout.write(f"{s}")
                        fout.write('\n')
                        break
            else:
                if list(r[:(len(r) // 2)]) == list(reversed(r[(len(r) // 2):])):

                    every += 1
                    if every == 2:
                        count += 1
                        fout.write(f"{s}")
                        fout.write('\n')
                        break
fout.close()

