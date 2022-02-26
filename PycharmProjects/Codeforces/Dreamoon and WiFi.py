n = input()
nn = input()
arr = list(n)
arr2 = list(nn)
tea = 0
tea2 = 0
drug = []
for k in arr:
    if k == '+':
        tea += 1
    else:
        tea -= 1
for k in arr2:
    if k == '+':
        tea2 += 1
    else:
        tea2 -= 1
if '?' not in nn:
    if tea == tea2:
        print(1.00)
    else:
        print(0.00)
else:
    z = arr2.count('?')
    for xd in range(z, -z-1, -2):
        print(xd)
        drug.append(tea2+xd)
    an = drug.count(tea)
    print(an / len(drug))

    '''if gg == 1:
        drug.append(tea2 + 1)
        drug.append(tea2 - 1)
        an = drug.count(tea)
        print(an / len(drug))
    elif gg == 2:
        drug.append(tea2 + 0)
        drug.append(tea2 + 2)
        drug.append(tea2 - 2)
        an = drug.count(tea)
        print(an / len(drug))
    elif gg == 3:
        drug.append(tea2 + 1)
        drug.append(tea2 - 1)
        drug.append(tea2 + 3)
        drug.append(tea2 - 3)
        an = drug.count(tea)
        print(an / len(drug))
    elif gg == 4:
        drug.append(tea2 + 0)
        drug.append(tea2 + 2)
        drug.append(tea2 - 2)
        drug.append(tea2 + 4)
        drug.append(tea2 - 4)
        an = drug.count(tea)
        print(an / len(drug))
    elif gg == 5:
        drug.append(tea2 + 1)
        drug.append(tea2 - 1)
        drug.append(tea2 + 3)
        drug.append(tea2 - 3)
        an = drug.count(tea)
        print(an / len(drug))'''