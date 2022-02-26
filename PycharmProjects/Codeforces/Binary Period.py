for _ in range(int(input())):
    a = input()
    arr = list(a)
    z = len(a)
    zz = z * 2
    if len(set(arr)) == 1:
        print(a)
    elif arr[0] == '1':
        print(''.join(['1', '0'] * z))
    else:
        print(''.join(['0', '1'] * z))
