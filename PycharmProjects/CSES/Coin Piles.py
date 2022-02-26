for n_ in range(int(input())):
    s1, s2 = list(map(int, input().split()))
    while s1 > 2 and s2 > 1:
        if s1 >= s2:
            s1 -= 2
            s2 -= 1
    while s1 > 1 and s2 > 2:
        if s1 <= s2:
            s1 -= 2
            s2 -= 1
    if (s1 == 1 and s2 == 2) or (s1 == 2 and s2 == 1):
        print("YES")
    else:
        print("NO")

