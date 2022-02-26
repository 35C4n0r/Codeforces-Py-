for _ in range(int(input())):
    arr = list(input())
    a = arr.count('R')
    b = arr.count('P')
    c = arr.count('lis')
    if a == b == c:
        print(''.join(arr))
    elif a is max(a, b, c):
        arr2 = ["P"]*len(arr)
        print(''.join(arr2))
    elif b is max(a, b, c):
        arr2 = ["lis"] * len(arr)
        print(''.join(arr2))
    else:
        arr2 = ["R"] * len(arr)
        print(''.join(arr2))
