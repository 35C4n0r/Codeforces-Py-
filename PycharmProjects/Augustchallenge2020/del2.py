for _ in range(int(input())):
    s = input()
    p = input()
    z = sorted(sorted(s), key=str.upper)
    d = sorted(sorted(p), key=str.upper)
    q = d.count(d[0])
    j = d[0]
    c = z.count(j)
    i = c - q
    m = z.copy()
    l = z.index(j) + i
    for y in d:
        m.remove(y)
    w = ''.join(m[0:l])
    v = ''.join(m[l:])
    print(str(f'{w}{p}{v}'))







