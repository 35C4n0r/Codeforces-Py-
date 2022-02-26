for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ii = 0
    for g in arr:
        if g == k/2:
            if ii == 0:
                print(1, end=" ")
                ii = 1
            else:
                print(0, end=" ")
                ii = 0
        elif g > k/2:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
