for _ in range(int(input())):
    n, o = list(map(str, input().split()))
    n = int(n)
    if n%2 == 0:
        if o == 'P':
            print('PewDiePie')
        else:
            print("T-Series")
    else:
        if o == 'P':
            print("T-Series")
        else:
            print('PewDiePie')