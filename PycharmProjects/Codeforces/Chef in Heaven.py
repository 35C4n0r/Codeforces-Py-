for _ in range(int(input())):
    n = int(input())
    arr = list(input())
    #print(lis)
    good = 0
    bad = 0
    f = True
    for k in arr:
        if k == '1':
            good += 1
        else:
            bad += 1
        if good >= bad:
            print("YES")
            f = False
            break
    if f:
        print("NO")
