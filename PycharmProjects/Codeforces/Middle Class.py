for _ in range(int(input())):
    n, x = map(int, input().split())
    l = [int(x) for x in input().split()]
    l.sort()
    if sum(l) >= n*x:
        print(n)
    elif l[-1] < x:
        print("0")
    else:
        c, d = 0, 0
        for i in range(n-1, 0, -1):
            if l[i] >= x:
                c += 1
                d += l[i]-x
            else:
                if l[i]+d >= x:
                    c += 1
                    d = d-x+l[i]
        print(c)
