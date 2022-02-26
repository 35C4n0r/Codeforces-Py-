"""
ID: jay20ma1
LANG: PYTHON3
TASK: palsquare
"""


def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))

# number to a base 'base' and
def fromDeci(res, base, inputNum):
    index = 0  # Initialize index of result

    # Convert input number is given base
    # by repeatedly dividing it by base
    # and taking remainder
    while (inputNum > 0):
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)

        # Reverse the result
    res = res[::-1]

    return res


fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
n = int(fin.readline())
for k in range(1, 301):
    #res = str((int(''.join(list(f'{k**2}')), n)))
    #print(list(res[:(len(res)//2) + 1]), list(res[(len(res)//2) + 1:])[::-1])
    r = str(fromDeci("", n, k**2))
    #print(r)
    #print(list(r[:(len(r)//2)]), list(reversed(r[(len(r)//2):])))
    #print(r)
    #print(list(r[: len(r)//2]), list(reversed(r[(len(r)//2)+1:])))
    if len(r) == 1:
        fout.write(f"{fromDeci('', n, k)} {r}")
        fout.write('\n')
    else:
        if len(r) % 2 != 0:
            if list(r[: len(r)//2]) == list(reversed(r[(len(r)//2)+1:])):
                fout.write(f"{fromDeci('', n, k)} {r}")
                fout.write('\n')
        else:
            if list(r[:(len(r)//2)]) == list(reversed(r[(len(r)//2):])):
                fout.write(f"{fromDeci('', n, k)} {r}")
                fout.write('\n')
fout.close()
