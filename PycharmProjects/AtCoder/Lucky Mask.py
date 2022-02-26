a, b = list(map(int, input().split()))
while True:
    a += 1
    sta = str(a)
    m = ""
    n = 0
    for i in range(len(sta)):
        if sta[i] == '4' or sta[i] == '7':
            m += sta[i]
    if len(m) > 0:
        n = int(m)

    if n == b:
        print(a)
        break
