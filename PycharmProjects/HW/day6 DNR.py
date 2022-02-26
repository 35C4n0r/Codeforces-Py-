t = int(input())
for _ in range(t):
    line = input()
    first = ""
    second = ""

    for i, c in enumerate(line):
        if i % 2 == 0:
            first += c
        else:
            second += c
    print (first, second)


#or use this


for N in range(int(input())):
    S = input()
    print(S[0: :2], S[1: :2])