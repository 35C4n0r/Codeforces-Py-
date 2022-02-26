for _ in range(int(input())):
    pc, pr = list(map(int, input().split()))
    countc = 0
    countr = 0
    c = 0
    r = 0
    if pc % 9 > 0:
        countc += (pc // 9) + 1
    else:
        countc += pc // 9

    if pr % 9 > 0:
        countr += (pr // 9) + 1
    else:
        countr += pr // 9

    if countr <= countc:
        print(f"{1} {countr}")
    elif countc == len(str(pc)):
        print(f"{0} {countc}")
    elif countr == len(str(pr)):
        print(f"{1} {countr}")
    elif countc < countr:
        print(f"{0} {countc}")

