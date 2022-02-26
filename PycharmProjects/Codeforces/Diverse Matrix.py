r, c = list(map(int,input().split()))
if r == 1 and c == 1:
    print(0)
elif r == 1:
    for i in range(2, c+2):
        print(i, end=" ")
    print()
elif c == 1:
    for j in range(2,r+2):
        print(j,end=" ")
    print()
else:
    for i in range(c+1, r+c+1):
        for j in range(1, c+1):
            print(i*j, end=" ")
        print()
