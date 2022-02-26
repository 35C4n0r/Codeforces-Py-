for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    arr = list("EQUINOX")
    s = 0
    an = 0
    for _ in range(n):
        ss = list(input())
        if ss[0] in arr:
            s += a
        else:
            an += b
    if s > an:
        print('SARTHAK')
    elif an > s:
        print("ANURADHA")
    else:
        print("DRAW")
        